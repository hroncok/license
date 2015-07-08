import pytest

from license import License
from license import register, find


class TestDB(object):

    def test_register_no_id(self):
        '''
        Test that License classes cannot be registered without id
        '''
        class FooLicense(License):
            pass

        with pytest.raises(AttributeError):
            register(FooLicense)

    def test_register_and_find(self):
        '''
        Test that License classes can be registered with id
        '''
        class FooLicense(License):
            id = 'FOO'

        register(FooLicense)
        assert find('FOO') == FooLicense

    def test_nonexisting(self):
        '''
        Test that non-existing license cannot be found
        '''
        with pytest.raises(KeyError):
            find('This is not an existing SPDX identifier')
