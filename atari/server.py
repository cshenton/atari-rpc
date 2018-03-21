"""The Atari server."""
import gym
import proto

from atari.name import

DEFAULT_ENVIRONMENT = 'Pong-v4'

class Server(proto.AtariServicer):
    """Server is responsible for setting and progressive the active environment.

    Attributes:
        environment (gym.Environment): The current active environment.
    """
    def __init__(self):
        self.environment = gym.make(DEFAULT_ENVIRONMENT)

    def Start(self, request, context):
        """Start initialises and resets the requested environment."""
        env_name =
        pass

    def Step(self, request, context):
        """Step acts on the active environment and returns the new state."""
        pass