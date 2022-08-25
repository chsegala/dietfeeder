import logging

# region application constants

LOG_LEVEL = logging.DEBUG
GPIO_WARNINGS = False
STEPPER_TIMEOUT = 15  # in seconds

# endregion

# region board constants

STEPPER_PINS = [8, 10, 12, 16]
BARREL_INTERRUPT_PIN = 18

# endregion
