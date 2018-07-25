#!/usr/bin/env python3

"""
Copyright (c) 2015 Alan Yorinks All rights reserved.
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU  General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.
You should have received a copy of the GNU  General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

# import the API class


from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

speedOfSound = .0343000  # cm/us, according to google

deColores = {'black': {'r': 0, 'g': 0, 'b': 0}, 'green': {'r': 0, 'g': 80, 'b': 0}, 'yellow': {'r': 100, 'g': 30, 'b': 0},
             'red': {'r': 100, 'g': 0, 'b': 0}}


# ping callback function
def trigger_ping():

    pingData = board.sonar_data_retrieve(7)
    if pingData is not None:
        pingDistance = pingData * 0.5 * speedOfSound  # this computes the approximate distance in cm
        print('{0} cm'.format((f"{pingDistance:.2f}")))  # this prints the distance, rounding the float to 2 decimal places

        if 5.0 > pingDistance > 0.1:
            board.analog_write(3, deColores['red']['r'])
            board.analog_write(5, deColores['red']['g'])
            board.analog_write(6, deColores['red']['b'])
        elif 5.0 <= pingDistance < 10.0:
            board.analog_write(3, deColores['yellow']['r'])
            board.analog_write(5, deColores['yellow']['g'])
            board.analog_write(6, deColores['yellow']['b'])
        elif pingDistance > 10.0:
            board.analog_write(3, deColores['green']['r'])
            board.analog_write(5, deColores['green']['g'])
            board.analog_write(6, deColores['green']['b'])
        else:
            board.analog_write(3, deColores['black']['r'])
            board.analog_write(5, deColores['black']['g'])
            board.analog_write(6, deColores['black']['b'])
    else:
        board.analog_write(3, deColores['black']['r'])
        board.analog_write(5, deColores['black']['g'])
        board.analog_write(6, deColores['black']['b'])


# create a PyMata instance
board = PyMata3(2)

# configure 4 pins for 4 SONAR modules
board.sonar_config(7, 8)

# configure RGB LED pins to be digital outputs
board.set_pin_mode(3, Constants.PWM)
board.set_pin_mode(5, Constants.PWM)
board.set_pin_mode(6, Constants.PWM)

while True:
    trigger_ping()
    board.sleep(.2)

board.shutdown()
