from . import License
from . import register


class MITLicense(License):
    '''
    The MIT license
    '''
    id = 'MIT'
    rpm = 'MIT'
    python = 'License :: OSI Approved :: MIT License'
    url = 'http://opensource.org/licenses/MIT'


register(MITLicense)
