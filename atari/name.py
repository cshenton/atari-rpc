"""Compatibility layer between proto.Environment and gym name strings."""

def make_name(env):
    """Returns a gym compatible name, like 'Pong-ram-v0'.

    Args:
        env (proto.Environment): A proto environment message.

    Returns:
        string: A valid gym environment name.
    """
    name = ''
    words = env.game.name.split('_')

    for w in words:
        name += w.capitalize()

    if env.game_type.name == 'RAM':
        name += '-ram'

    name += '-v'
    name += str(env.version)

    return name
