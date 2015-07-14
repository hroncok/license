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
        template = cls.jinja_env.get_template(cls.id)
        return template.render(**kwargs)
