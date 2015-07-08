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
    def render(cls, path):
        cls.check()
        print('TODO Render {} to {}'.format(cls, path))
