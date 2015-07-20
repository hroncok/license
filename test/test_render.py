# -*- coding: utf-8 -*-
from datetime import date

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
        assert str(date.today().year) in text
        assert 'Permission is hereby granted' in text

    @pytest.mark.parametrize('id', ('GPL-2.0+', 'GPL-2.0', 'GPL-3.0+', 'GPL-3.0'))
    def test_header(self, id):
        '''
        Test that License classes with header render it
        '''
        email = 'peter@foo.org'
        header = license.find(id).header(name='Petr Foo', email=email)
        assert email in header
        assert str(date.today().year) in header
        assert 'This program is free software' in header

    def test_header_no_template(self):
        '''
        Test that License classes without header templates raise AttributeError during .header()
        '''
        with pytest.raises(AttributeError):
            header = license.find('MIT').header()

    def test_render_undefined(self):
        '''
        Test that License classes will fail to render without all variables defined
        '''
        with pytest.raises(jinja2.UndefinedError):
            license.find('MIT').render(name='xx')
