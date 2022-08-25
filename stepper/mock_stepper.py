import logging as log
from time import sleep

from stepper.base_stepper import BaseStepper


class MockStepper(BaseStepper):
    """
    Mock implementation to only print the
    value sent to stepper motor
    """

    def __init__(self, pins: list[int]):
        log.info('Initializing mock stepper')
        super().__init__(pins)

    def _rotate(self, state: list[int]):
        log.info('state ==> %s', state)
        super()._rotate(state)
