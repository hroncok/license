from .base import License


class MITLicense(License):
    '''
    The MIT license
    '''
    id = 'MIT'
    rpm = 'MIT'
    python = 'License :: OSI Approved :: MIT License'
    url = 'http://opensource.org/licenses/MIT'


class GPLv3LaterLicense(License):
    '''
    GNU General Public License v3.0 or later
    '''
    id = 'GPL-3.0+'
    rpm = 'GPLv3+'
    python = 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    url = 'http://www.gnu.org/licenses/gpl-3.0.html'


class GPLv3OnlyLicense(GPLv3LaterLicense):
    '''
    GNU General Public License v3.0 only
    '''
    id = 'GPL-3.0'
    rpm = 'GPLv3'
    python = 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
