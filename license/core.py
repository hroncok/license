from . import base
from . import licenses


_db = {}
_indexes = {}


def register(cls):
    '''
    Register a license class to the database
    '''
    try:
        subclass = issubclass(cls, base.License)
    except TypeError:
        subclass = False
    if not subclass:
        raise TypeError('register() got something that\'s not a subclass of License')

    if cls is base.License:
        raise TypeError('register() needs a subclass of License, not License itself')

    try:
        _db[cls.id] = cls
    except AttributeError:
        raise AttributeError('{} has no mandatory \'id\' attribute'.format(cls.__name__))


def find(id):
    '''
    Find a license class with the given SPDX id
    '''
    try:
        return _db[id]
    except KeyError:
        raise KeyError('License with SPDX id {} not found'.format(id))


def build_index(key):
    '''
    Builds an index of all the licenses with the given key,
    makes find_by_key() faster
    '''
    _indexes[key] = {}
    for cls in _db.values():
        if hasattr(cls, key):
            value = getattr(cls, key)
            if value not in _indexes[key]:
                _indexes[key][value] = []
            _indexes[key][value].append(cls)


def delete_index(key):
    '''
    Deletes the index of all the licenses with the given key,
    will do nothing if such index does not exist
    '''
    if key in _indexes:
        del _indexes[key]


def find_by_function(function, multiple=True):
    '''
    Finds a license or licenses for which the given function equals True
    The function should take one argumnet, the License class, and return Boolean-ish
    the multiple argument behaves exactly the same as with find_by_key()
    '''
    results = []
    for cls in _db.values():
        if function(cls):
            if not multiple:
                return cls
            results.append(cls)

    if not multiple:
        raise KeyError('No such license found')
    return results


def find_by_key(key, value, multiple=True):
    '''
    Finds a license with given value as a key
    If multiple is False, returns only the first result and raises KeyError if non found
    If multiple is True, returns an array of results (might be empty)
    Calling build_index(key) might speed things up if you want to search by the same key often
    '''
    if key in _indexes:
        try:
            if multiple:
                return _indexes[key][value]
            return _indexes[key][value][0]
        except KeyError:
            if multiple:
                return []
            raise KeyError('No such license found')

    def function(cls):
        return hasattr(cls, key) and getattr(cls, key) == value

    return find_by_function(function, multiple=multiple)


def iter():
    '''
    Get an iterable object of all licenses
    '''
    try:
        return _db.itervalues()
    except AttributeError:
        return _db.values()


def autoregister(module=licenses, ignore=[]):
    '''
    Automatically register all licenses from a given module
    '''
    for name, cls in vars(module).items():
        if cls not in ignore:
            try:
                register(cls)
            except TypeError:
                pass
