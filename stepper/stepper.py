import os
from datetime import datetime
from threading import Thread
from time import sleep

from utils.constants import STEPPER_TIMEOUT

from stepper.device_stepper import DeviceStepper
from stepper.mock_stepper import MockStepper


class Stepper:
    _t: Thread = None
    _running: bool = False
    _sleep_secs = 0.001

    def __init__(self, pins: list[int]) -> None:
        if (os.getenv('ENVIRONMENT') == 'dev'):
            self._sleep_secs = 0.5  # run a little slower to debug
            self.stepper = MockStepper(pins)
        else:
            self.stepper = DeviceStepper(pins)

    def _rotate_forever(self):
        rotating_since = datetime.today()
        while self._running:
            self.stepper.rotate()
            sleep(self._sleep_secs)

            rotating_for = datetime.today() - rotating_since
            if (rotating_for.total_seconds() > STEPPER_TIMEOUT):
                self.stop()
                break

        self._t = None

    def is_running(self):
        return self._running

    def rotate(self):
        if not self._t:
            self._running = True
            self._t = Thread(target=self._rotate_forever)
            self._t.start()

    def stop(self):
        if self._t and self._running:
            self._running = False
