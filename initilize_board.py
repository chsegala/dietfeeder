import os

from utils.constants import GPIO_WARNINGS

def initialize_board():
    if(os.getenv('ENVIRONMENT') != 'dev'):
        from OPi import GPIO
        from orangepi.pc import BOARD
        
        GPIO.setwarnings(GPIO_WARNINGS)
        GPIO.setmode(BOARD)

if __name__ == "main":
    initialize_board()