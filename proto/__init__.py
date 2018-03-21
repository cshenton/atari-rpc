"""Wrapper package for generated proto, grpc code."""
from proto.atari_pb2 import (
    Action,
    Environment,
    Game,
    GameType,
    Observation,
    State,
)
from proto.atari_pb2_grpc import (AtariServicer)
from proto.atari_pb2_grpc import add_AtariServicer_to_server as register_server