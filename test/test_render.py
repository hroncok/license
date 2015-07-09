# -*- coding: utf-8 -*-
import jinja2
import pytest

import license


class TestRender(object):

    @pytest.mark.parametrize('name', ('Petr Foo', u'Petr Fóó'))
    def test_render(self, name):
        '''
        Test that License classes can render it's files
        '''
        email = 'peter@foo.org'

        text = license.find('MIT').render(name=name, email=email)

        assert name in text
        assert email in text
        assert 'Permission is hereby granted' in text

    def test_render_undefined(self):
        '''
        Test that License classes will fail to render without all variables defined
        '''
        with pytest.raises(jinja2.UndefinedError):
            license.find('MIT').render(name='xx')
