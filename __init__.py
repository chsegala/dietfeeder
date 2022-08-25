import logging
from time import sleep

from initilize_board import initialize_board
from inputs.interruptor import Interruptor
from mqtt_client.mqtt_client import MqttClient
from stepper.stepper import Stepper
from utils.constants import BARREL_INTERRUPT_PIN, LOG_LEVEL, STEPPER_PINS

logging.basicConfig(level=LOG_LEVEL)

# Initialize Board - if running on device
initialize_board()
stepper = Stepper(STEPPER_PINS)


def rotate_callback(payload: dict):
    if (payload['action'] == 'feed'):
        stepper.rotate()


def stop_callback():
    stepper.stop()


Interruptor(BARREL_INTERRUPT_PIN, stop_callback)

client = MqttClient()
client.sub(rotate_callback)

while True:
    try:
        sleep(1)
    # press ctrl+c for keyboard interrupt
    except KeyboardInterrupt:
        if (stepper.is_running()):
            stepper.stop()
        else:
            exit(0)
