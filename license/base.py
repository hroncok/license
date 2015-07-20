from datetime import date

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
    def _add_year_to_kwargs(cls, kwargs):
        if 'year' not in kwargs:
            kwargs['year'] = date.today().year
        return kwargs

    @classmethod
    def _check(cls):
        if cls == License:
            raise TypeError('This is a virtual class, do not call it\'s methods')

    @classmethod
    def render(cls, **kwargs):
        '''
        Render the LICENSE file
        '''
        cls._check()
        kwargs = cls._add_year_to_kwargs(kwargs)
        template = cls.jinja_env.get_template(cls.id)
        return template.render(**kwargs)

    @classmethod
    def header(cls, **kwargs):
        '''
        Render the LICENSE file
        '''
        cls._check()
        kwargs = cls._add_year_to_kwargs(kwargs)
        try:
            template = cls.jinja_env.get_template(cls.id + '__header')
            return template.render(**kwargs)
        except jinja2.TemplateNotFound:
            raise AttributeError('{} uses no header'.format(cls.name))


def custom_license_base_class(loader):
    '''
    A factory that generates a Custom License Base Class.
    Requires a jinja2.<something>Loader as an argument
    '''
    if not isinstance(loader, jinja2.loaders.BaseLoader):
        raise AttributeError('loader has to be a jinja2.<something>Loader instance')

    class CustomBaseLicense(License):
        jinja_env = jinja2.Environment(loader=loader, undefined=jinja2.StrictUndefined)

    return CustomBaseLicense
