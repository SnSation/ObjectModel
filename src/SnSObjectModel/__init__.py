# SnSObjectModel
from . import core

__all__ = ['core']

def new(base_objects=[], name='default_ObjectModel', cache={}):
    new_ObjectModel = core.ObjectModel(base_objects, name, cache)
    return new_ObjectModel