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


class LGPLv21LaterLicense(License):
    '''
    GNU Lesser General Public License v2.1 or later
    '''
    id = 'LGPL-2.1+'
    rpm = 'LGPLv2+'
    python = 'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)'
    url = 'http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html'


class LGPLv21OnlyLicense(LGPLv21LaterLicense):
    '''
    GNU Lesser General Public License v2.1 only
    '''
    id = 'LGPL-2.1'
    rpm = 'LGPLv2'
    python = 'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)'


class LGPLv3LaterLicense(License):
    '''
    GNU Lesser General Public License v3.0 or later
    '''
    id = 'LGPL-3.0+'
    rpm = 'LGPLv3+'
    python = 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)'
    url = 'http://www.gnu.org/licenses/lgpl-3.0.html'


class LGPLv3OnlyLicense(LGPLv3LaterLicense):
    '''
    GNU Lesser General Public License v3.0 only
    '''
    id = 'LGPL-3.0'
    rpm = 'LGPLv3'
    python = 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)'


class AGPLv3LaterLicense(License):
    '''
    GNU Affero General Public License v3.0 or later
    '''
    id = 'AGPL-3.0+'
    rpm = 'AGPLv3+'
    python = 'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)'
    url = 'http://www.gnu.org/licenses/agpl-3.0.html'


class AGPLv3OnlyLicense(AGPLv3LaterLicense):
    '''
    GNU Affero General Public License v3.0 v3.0 only
    '''
    id = 'AGPL-3.0'
    rpm = 'AGPLv3'
    python = 'License :: OSI Approved :: GNU Affero General Public License v3'


class Apachev1License(License):
    '''
    Apache License Version 1.0
    '''
    id = 'Apache-1.0'
    rpm = 'ASL 1.0'
    python = 'License :: OSI Approved :: Apache Software License'
    url = 'https://www.apache.org/licenses/LICENSE-1.0'


class Apachev11License(Apachev1License):
    '''
    Apache License Version 1.1
    '''
    id = 'Apache-1.1'
    rpm = 'ASL 1.1'
    url = 'https://www.apache.org/licenses/LICENSE-1.1'


class Apachev2License(Apachev1License):
    '''
    Apache License Version 2.0
    '''
    id = 'Apache-2.0'
    rpm = 'ASL 2.0'
    url = 'https://www.apache.org/licenses/LICENSE-2.0'
