from OPi import GPIO
from stepper.base_stepper import BaseStepper

import logging


class DeviceStepper(BaseStepper):
    """
    Mock implementation to only print the
    value sent to stepper motor
    """

    def __init__(self, pins: list[int]):
        logging.info('Initializing device stepper')

        GPIO.setup(pins, GPIO.OUT)
        self.pins = pins
        super().__init__(pins)

    def _rotate(self, state: list[int]):
        for i, p in enumerate(self.pins):
            GPIO.output(p, state[i])
        super()._rotate(state)
