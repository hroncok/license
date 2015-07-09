import pytest

from license import License
from license import register, find
from license import find_by_key, build_index, delete_index
from license.licences import MITLicense


KEYS = ('rpm', 'name', 'url')


class TestRegisterFind(object):
    '''
    Test register() and find()
    '''

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

    @pytest.mark.parametrize('id', ('MIT',))
    def test_exisitng(self, id):
        '''
        Test that an exisitng license can be found
        '''
        assert find(id).id == id


class TestFindByKeyWithoutIndex(object):
    '''
    Tests for find_by_key() when no index has been built
    '''

    @pytest.mark.parametrize('key', KEYS)
    def test_find_by_key_multiple(self, key):
        '''
        Test that it is possible to find the license by various keys
        '''
        value = getattr(MITLicense, key)
        results = find_by_key(key, value)
        assert results == [MITLicense]

    @pytest.mark.parametrize('key', KEYS)
    def test_find_by_key_single(self, key):
        '''
        Test that it is possible to find the license by various keys
        '''
        value = getattr(MITLicense, key)
        result = find_by_key(key, value, multiple=False)
        assert result == MITLicense

    @pytest.mark.parametrize('key', KEYS)
    def test_find_by_key_multiple_wrong(self, key):
        '''
        Test that when finding multiple results, empty list is returned when nothing found
        '''
        value = 'nonexistent value'
        results = find_by_key(key, value)
        assert results == []

    @pytest.mark.parametrize('key', KEYS)
    def test_find_by_key_single_wrong(self, key):
        '''
        Test that when finding single result, KeyError is risen when nothing found
        '''
        value = 'nonexistent value'
        with pytest.raises(KeyError):
                result = find_by_key(key, value, multiple=False)


class TestFindByKeyWithIndex(TestFindByKeyWithoutIndex):
    '''
    Tests for find_by_key() when the index has been built
    '''

    @classmethod
    def setup_class(cls):
        for key in KEYS:
            build_index(key)

    @classmethod
    def teardown_class(cls):
        for key in KEYS:
            delete_index(key)
