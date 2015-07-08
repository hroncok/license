import pytest

from license import License
from license import register


class TestDB(object):

    def test_register_no_id(self):
        '''
        Test that License classes cannot be registered without id
        '''
        class FooLicense(License):
            pass

        with pytest.raises(AttributeError):
            register(FooLicense)

    def test_register(self):
        '''
        Test that License classes can be registered with id
        '''
        class FooLicense(License):
            id = 'FOO'

        register(FooLicense)
