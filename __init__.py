from .base import BaseClass

__all__ = ['BaseClass']

def new(profile_name='default'):
    new_object = BaseClass(profile=profile_name)
    return new_object