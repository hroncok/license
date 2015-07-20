from .base import License


class MITLicense(License):
    '''
    The MIT license
    '''
    id = 'MIT'
    rpm = 'MIT'
    python = 'License :: OSI Approved :: MIT License'
    url = 'http://opensource.org/licenses/MIT'


class BSD2ClauseLicense(License):
    '''
    BSD 2-clause "Simplified" License
    '''
    id = 'BSD-2-Clause'
    rpm = 'BSD'
    python = 'License :: OSI Approved :: BSD License'
    url = 'http://opensource.org/licenses/BSD-2-Clause'


class BSD3ClauseLicense(BSD2ClauseLicense):
    '''
    BSD 3-clause "New" or "Revised" License
    '''
    id = 'BSD-3-Clause'
    url = 'http://opensource.org/licenses/BSD-3-Clause'


class GPLv2LaterLicense(License):
    '''
    GNU General Public License v2.0 or later
    '''
    id = 'GPL-2.0+'
    rpm = 'GPLv2+'
    python = 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv2+)'
    url = 'http://www.gnu.org/licenses/old-licenses/gpl-2.0.html'


class GPLv2OnlyLicense(GPLv2LaterLicense):
    '''
    GNU General Public License v2.0 only
    '''
    id = 'GPL-2.0'
    rpm = 'GPLv2'
    python = 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'


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
