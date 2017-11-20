

from inspect import getfullargspec


def save_args(values):
    for i in getfullargspec(values['self'].__init__).args[1:]:
        setattr(values['self'], i, values[i])
