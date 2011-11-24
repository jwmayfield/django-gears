missing = object()


class cached_property(object):

    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.__module__ = func.__module__

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, missing)
        if value is missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


def first(function, iterable):
    if function is None:
        function = bool
    for item in iterable:
        if function(item):
            return item
    raise ValueError('No suitable value found.')


def first_or_none(function, iterable):
    try:
        return first(function, iterable)
    except ValueError:
        pass
