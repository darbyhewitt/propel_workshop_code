'''
    FirmataPlus example program
    connect RGB LED to pins 3, 5, and 6 (R, G, and B, respectively)
    Darby Hewitt 7/24/2018
'''

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


def pins_6_5_3_pwmSweep():
    """
    Set digital pin 6 as a PWM output and set its output value to 128
    @return:
    """
    # instantiate the pymata_core API
    board = PyMata3()

    # set the pin modes
    board.set_pin_mode(6, Constants.PWM)
    board.set_pin_mode(5, Constants.PWM)
    board.set_pin_mode(3, Constants.PWM)

    deColores = [ \
                 {'r':256, 'g':0, 'b':0}, \
                 {'r':0, 'g':256, 'b':0}, \
                 {'r':0, 'g':0, 'b':256}, \
                 {'r':256, 'g':256, 'b':0}, \
                 {'r':256, 'g':0, 'b':256}, \
                 {'r':0, 'g':256, 'b':256}, \
                 {'r':256, 'g':256, 'b':256} \
                 ]

    for color in range(len(deColores)):
        for r in range(1, 100, 2):
            board.analog_write(3, int(.01*r*deColores[color]['r']))
            board.analog_write(5, int(.01*r*deColores[color]['g']))
            board.analog_write(6, int(.01*r*deColores[color]['b']))
            board.sleep(.03)
        for r in range(99, 0, -2):
            board.analog_write(3, int(.01*r*deColores[color]['r']))
            board.analog_write(5, int(.01*r*deColores[color]['g']))
            board.analog_write(6, int(.01*r*deColores[color]['b']))
            board.sleep(.03)

    # reset the board and exit
    board.shutdown()

if __name__ == "__main__":
    pins_6_5_3_pwmSweep()