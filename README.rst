license
=======

license is a Python library providing some metadata about common free software licenses, such as
GNU GPL, MIT and others. It is compatible with Python 2.7 and Python 3.

Basic usage
-----------

To get a license, you can use `SPDX license identifier <http://spdx.org/licenses/>`_:

.. code-block:: python

    import license
    mit = license.find('MIT')

Each license is a static class providing a few properties:

* ``id`` - the SPDX identifier
* ``name`` - a human readable name of the license
* ``rpm`` - `license identifier used in Fedora, RHEL and CentOS RPMs <https://fedoraproject.org/wiki/Licensing:Main#Good_Licenses>`_
* ``python`` - `PyPI classifier <https://pypi.python.org/pypi?%3Aaction=list_classifiers>`_
* ``url`` - link to a license description or website

.. code-block:: python

    mit.python
    'License :: OSI Approved :: MIT License'

License classes also offer a static method ``render()`` that will output the entire license text.
Some variables have to be passed to it, usually ``name``, ``email`` and optional ``year``
(current year is used when omitted).

.. code-block:: python

    mit.render(name='Petr Foo', email='petr@foo.org')
    '''The MIT License (MIT)
    
    Copyright (c) 2015 Petr Foo <petr@foo.org>
    
    Permission is hereby granted... (snip)'''

Some licenses (such as the ones from GPL family) also have a header text, that's supposed to be
added to each source file. ``header()`` is used to render that, but be careful, if the license does
not use special header, ``AttributeError`` is risen.

.. code-block:: python

    mit.header(name='Petr Foo', email='petr@foo.org')
    AttributeError: The MIT license uses no header

If you want to search the licenses by some other key, you can:

.. code-block:: python

    bsd = license.find_by_key('rpm', 'BSD')
    bsd
    [license.licenses.BSD3ClauseLicense, license.licenses.BSD2ClauseLicense]

``bsd`` is now a list, because unlike SPDX identifiers, other keys might not always be unique. If
you only need the first license with such identifier, you can pass ``multiple=False`` to
``find_by_key()``:

.. code-block:: python

    bsd = license.find_by_key('rpm', 'BSD', multiple=False)
    bsd
    license.licenses.BSD3ClauseLicense

If such license is not found, you'll get ``KeyError`` instead, the same as with regular ``find()``.

In case you would like to perform a lot of searches by some key, you can build and index, which
should (in theory) make the searches faster (no measurements have been performed).

.. code-block:: python

    license.build_index('rpm')

In case you want to get rid of an index, use ``license.delete_index(key)``. It is safe to call it
even if the index does not exist.

It is also possible to use ``find_by_function()`` to find licenses that match a certain expression.
The function should accept one argument (the license class) and return True if the license is
supposed to be in the results:

.. code-block:: python

    osi = license.find_by_function(lambda l: l.python.startswith('License :: OSI Approved :: '))

Again, it returns a list and has ``multiple`` argument to change that.

In case a simple function is not enough, you can iterate over all the license with
``license.iter()``:

.. code-block:: python

    for cls in license.iter():
        # do something

Adding licenses
---------------

The current license list is in no way much extensive, so maybe your favorite license is not in
there. If you wish to change that, add the license to ``license/licenses.py`` and a template(s) to
``license/templates``, and send a `pull request on GitHub
<https://github.com/hroncok/license/pulls>`_. See the current licenses to learn how to do it.
A license class looks like this:

.. code-block:: python

    class AGPLv3LaterLicense(license.base.License):
        '''
        GNU Affero General Public License v3.0 or later
        '''
        id = 'AGPL-3.0+'
        rpm = 'AGPLv3+'
        python = 'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)'
        url = 'http://www.gnu.org/licenses/agpl-3.0.html'

One license can inherit from other and omit the keys that are equal. Note that the docstring is
important and it is used as ``name`` property. License template is named as ``id``, header template
is named with ``__header`` suffix.

If you wish to add custom licenses in your code, you can do that as well. If you won't use
``render()`` or ``header()``, the thing is simple. Just define such class anywhere and call
``license.register()`` on it.

However, if you would then call ``render()`` or ``header()``, the template would hove not been
found. In that case, you have to create a *Custom Base License* with a ``jinja2`` template loader.

.. code-block:: python

    CustomBaseLicense = license.base.custom_license_base_class(loader=jinja2.FileSystemLoader('path/to/templates'))
    
    class CustomLicense(CustomBaseLicense):
        ...

    license.register(CustomLicense)

The ``loader`` can be any valid `jinja2 loader <http://jinja.pocoo.org/docs/dev/api/#loaders>`_.
If you wish to register multiple classes at once, you can use ``license.autoregister()`` that will
register all classes present in given module. You will not want to register your
``CustomBaseLicense``, so you'll pass it in the ``ignore`` argument.

.. code-block:: python
    
    license.autoregister(sys.modules[__name__], ignore=[CustomBaseLicense])

Note that if you add custom licenses and use ``license.build_index()``, you want to build the index
after registering them. Calling ``build_index()`` multiple times is safe.

(Possibly) Frequently Asked Questions
-------------------------------------

Why are licenses represented as subclasses and not instances of ``License``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This way, it is easier to inherit data between multiple licenses. The definition of classes is
easier maintainable and readable.

Isn't ``license`` a reserved name?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, it is, it prints the Python's license. Possibly something you would only use in an interactive
Python console. By importing this library, you are overriding it. We could have named the library
with something cool and unique, such as ``licenraptor``, but we wanted to make the name as easy as
possible. In case you don't like this, you can always do ``import license as somethignelse``.

Aren't there already Python tools that can render license texts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, they are. However all of them are command line utilities and provide no API for Python
programmers.

* `choosealicense-cli <https://pypi.python.org/pypi/choosealicense-cli>`_
* `licenser <https://pypi.python.org/pypi/licenser>`_
* `licen <https://pypi.python.org/pypi/licen>`_
* `garnish <https://pypi.python.org/pypi/garnish>`_
