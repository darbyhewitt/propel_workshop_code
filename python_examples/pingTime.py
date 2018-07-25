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

speedOfSound = .0343000  # cm/us, according to google


# ping callback function
def cb_ping(data):
    print(str(data[1]) + ' us')  # this prints the raw time delay
    # pingDistance = data[1]*0.5*speedOfSound         # this computes the approximate distance in cm
    # print('{0} cm'.format((f"{pingDistance:.2f}"))) # this prints the distance, rounding the float to 2 decimal places


# create a PyMata instance
board = PyMata3(2)

# configure 4 pins for 4 SONAR modules
board.sonar_config(7, 8, cb_ping)

while True:
    board.sleep(.1)

board.shutdown()
