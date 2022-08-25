import abc


class BaseStepper(metaclass=abc.ABCMeta):
    """
    Base class to fix contract of different implementations of steppers
    namelly mock stepper (test only) and the physical embedded device
    enabled stepper
    """

    # current state of stepper
    state = [1, 0, 0, 1]

    @abc.abstractmethod
    def __init__(self, pins: list[int]):
        pass

    def rotate(self):
        """
        Rotates the step motor
        """
        self._rotate(self.state)
        self.state = BaseStepper._rotate_state(self.state)

    @abc.abstractmethod
    def _rotate(self, state: list[int]):
        """
        Stub to implement actual motor rotations based of the state
        """
        return

    @classmethod
    def _rotate_state(cls, curr_state):
        return curr_state[-1:] + curr_state[:-1]
