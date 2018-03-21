"""The Atari server."""
import gym
import proto

from atari.name import make_name


DEFAULT_ENVIRONMENT = 'Pong-v4'


class Server(proto.AtariServicer):
    """Server is responsible for setting and progressive the active environment.

    Attributes:
        environment (gym.Environment): The current active environment.
    """

    def __init__(self):
        self.environment = gym.make(DEFAULT_ENVIRONMENT)

    def Start(self, request, context):
        """Start initialises and resets the requested environment.

        Args:
            request (proto.Environment): The environment to start.
            context (grpc.Context): The request context.

        Returns:
            proto.Observation: The first observation from the reset environment.
        """
        try:
            name = make_name(request)
            new_env = gym.make(name)
            obs = new_env.reset()
        except Error as e:
            raise ValueError("invalid environment name: %v".format(name))

        self.environment = new_env

        return proto.Observation(
            shape=list(obs.shape),
            values=obs.flatten.tolist(),
        )

    def Step(self, request, context):
        """Step acts on the active environment and returns the new state.

        Args:
            request (proto.Action): The action to take.
            context (grpc.Context): The request context.

        Returns:
            proto.Observation: The next state of the environment.
        """
        try:
            obs, reward, done, info = self.environment.step(request.value)
        except IndexError as e:
            max_action = int(str(x).split(' ')[-1]) - 1
            msg = "action must be between 0 and %v".format(max_action)
            raise ValueError(msg)

        return proto.State(
            observation=proto.Observation(
                shape=list(obs.shape),
                values=obs.flatten.tolist(),
            ),
            reward=reward,
            done=done,
            info=str(info),
        )