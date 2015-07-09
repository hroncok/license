import jinja2


class classproperty(object):
    '''
    Decorator for class property
    '''
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class LicenseClass(type):
    '''
    MetaClass for License classes
    '''

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class License(object):
    '''
    Base Virtual License
    '''

    __metaclass__ = LicenseClass

    jinja_env = jinja2.Environment(loader=jinja2.PackageLoader('license', 'templates'),
                                   undefined=jinja2.StrictUndefined)

    def __init__(self):
        raise TypeError('License classes are not about to be instantiated')

    @classproperty
    def name(cls):
        name = cls.__doc__
        if not name:
            raise AttributeError('{} has no docstring'.format(cls.__name__))
        return name.strip()

    @classmethod
    def check(cls):
        if cls == License:
            raise TypeError('This is a virtual class, do not call it\'s methods')

    @classmethod
    def render(cls, **kwargs):
        '''
        Render the LICENSE file
        '''
        cls.check()
        template = License.jinja_env.get_template(cls.id)
        return template.render(**kwargs)


_db = {}
_indexes = {}


def register(cls):
    '''
    Register a license class to the database
    '''
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


def find_by_key(key, value, multiple=True):
    '''
    Finds a license with given value as a key
    If multiple is False, returns only the first result and raises KeyError if non found
    If multiple is True, returns an array of results (might be empty)
    Calling build_index(key) might speed things up if you want to search by the same key often
    '''
    msg = 'No license with {}={} found'.format(key, value)

    if key in _indexes:
        try:
            if multiple:
                return _indexes[key][value]
            return _indexes[key][value][0]
        except KeyError:
            if multiple:
                return []
            raise KeyError(msg)

    results = []
    for cls in _db.values():
        if hasattr(cls, key) and getattr(cls, key) == value:
            if not multiple:
                return cls
            results.append(cls)

    if not multiple:
        raise KeyError(msg)
    return results


# Keep this at the end of file, otherwise it doesn't work
from .licences import *
