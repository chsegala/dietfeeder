import logging as log
from threading import Thread
from time import sleep

from OPi import GPIO


class Interruptor:
    def _check_edge(self, previous_state, curr_state):
        if(previous_state < curr_state):
            return GPIO.RISING
        return GPIO.FALLING

    def _check_event(self):
        while True:
            curr_state = GPIO.input(self._pin)
            if(curr_state != self._last_pin_state):
                log.info("Received interruption on pin %s", self._pin)

                detected_edge = self._check_edge(self._last_pin_state, curr_state)
                if(self._edge == GPIO.BOTH or self._edge == detected_edge):
                    self._callback()

            self._last_pin_state = curr_state
            sleep(0.01)

    def __init__(self, pin: int, callback: callable, edge = GPIO.FALLING):
        self._pin = pin
        self._callback = callback
        self._edge = edge

        log.info("Configuring interruptor at pin '%s'", self._pin)

        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._last_pin_state = GPIO.input(self._pin)

        Thread(target=self._check_event).start()
