import sys

import jinja2
import pytest

import license
from license import base


class TestLicenseClass(object):

    def test_no_instances(self):
        '''
        Test that instantiating License class raises TypeError
        '''
        with pytest.raises(TypeError):
            l = base.License()

    def test_no_instances_subclass(self):
        '''
        Test that instantiating a subclass of License class raises TypeError
        '''
        class FooLicense(base.License):
            pass

        with pytest.raises(TypeError):
            l = FooLicense()

    def test_docstring_is_name(self):
        '''
        Test that subclass'es docstring is successfully returned as name
        '''
        class FooLicense(base.License):
            '''
            Foo License
            '''

        assert FooLicense.name == 'Foo License'

    @pytest.mark.skipif(sys.version_info[0] == 3,
                        reason='unicode does not work on Py3k, str implementation is broken')
    @pytest.mark.parametrize('t', ('str', 'unicode'))
    def test_str(self, t):
        '''
        Test that string representation of License subclass is based on docstring
        '''
        class FooLicense(base.License):
            '''
            Foo License
            '''

        try:
            t = __builtins__[t]
        except TypeError:
            # happens on pypy
            t = getattr(__builtins__, t)

        assert t(FooLicense) == 'Foo License'

    def test_empty_docstring(self):
        '''
        Test that empty subclass'es docstring raises AttributeError when accesing the name
        '''
        class FooLicense(base.License):
            pass

        with pytest.raises(AttributeError):
            n = FooLicense.name

    def test_run_license_methods(self):
        '''
        Test that it is not possible to run render on License
        '''
        with pytest.raises(TypeError):
            base.License.render()


class TestCustomBaseLicenseFactory(object):

    @classmethod
    def setup_class(self):
        sbl = base.custom_license_base_class(loader=jinja2.FileSystemLoader('test/files'))

        class CustomLicense(sbl):
            '''Custom'''
            id = 'CUSTOM'
            url = 'URL'

        self.custom_cls = CustomLicense

    def test_render_custom_license_with_loader(self):
        '''
        Test we can render custom class with custom template loader
        '''
        assert self.custom_cls.render(text='foo') == 'START foo END'

    def test_register_find_custom_license(self):
        '''
        Test that custom license can be registered and found
        '''
        try:
            license.register(self.custom_cls)
            assert license.find('CUSTOM') == self.custom_cls
        finally:
            # unregister, just in case
            try:
                del license.core._db['CUSTOM']
            except:
                pass
