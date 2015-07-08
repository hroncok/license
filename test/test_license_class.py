import sys

import pytest

from license import License


class TestLicenseClass(object):

    def test_no_instances(self):
        '''
        Test that instantiating License class raises TypeError
        '''
        with pytest.raises(TypeError):
            l = License()

    def test_no_instances_subclass(self):
        '''
        Test that instantiating a subclass of License class raises TypeError
        '''
        class FooLicense(License):
            pass

        with pytest.raises(TypeError):
            l = FooLicense()

    def test_docstring_is_name(self):
        '''
        Test that subclass'es docstring is successfully returned as name
        '''
        class FooLicense(License):
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
        class FooLicense(License):
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
        class FooLicense(License):
            pass

        with pytest.raises(AttributeError):
            n = FooLicense.name

    def test_run_license_methods(self):
        '''
        Test that it is not possible to run render on License
        '''
        with pytest.raises(TypeError):
            License.render()
