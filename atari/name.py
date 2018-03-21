"""Compatibility layer between proto.Environment and gym name strings."""

def make_name(game, game_type, version):
    """Returns a gym compatible name, like 'Pong-ram-v0'.

    Arguments:
        game (proto.Game): A game enum value.
        game_type (proto.GameType): Game type (RAM or image).
        version (int): The environment version, base 0.
    """
    name = ''
    words = game.name.split('_')

    for w in words:
        name += w.capitalize()

    if game_type.name == 'RAM':
        name += '-ram'

    name += '-v'
    name += string(version)

    return name

