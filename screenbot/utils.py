

from inspect import getargspec


def save_args(values):
    for i in getargspec(values['self'].__init__).args[1:]:
        setattr(values['self'], i, values[i])
