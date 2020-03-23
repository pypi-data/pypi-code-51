from django.conf import settings
from psu_base.classes.Encryptor import Encryptor

__version__ = '0.12.2'
name = "psu_base"

default_app_config = 'psu_base.apps.PsuTemplateConfig'

# Default settings
_DEFAULTS = {
    'PSU_BASE_VERSION': __version__,
    'FINTI_URL': 'https://ws-test.oit.pdx.edu',
    'FINTI_SIMULATE_CALLS': False,  # Simulate Finti calls (i.e. when not on VPN)
    'FINTI_SAVE_RESPONSES': False,  # Save/record actual Finti responses for offline use?
    'AUTHORIZE_GLOBAL': False,      # Allow authorizing for other apps?

    # Admin Menu Items
    'PSU_BASE_ADMIN_LINKS': [
        {'url': "psu:test", 'label': "Status Page", 'icon': "fa-medkit"},
        {'url': "psu:emails", 'label': "Email Log", 'icon': "fa-envelope-o"},
        {'url': "psu:features", 'label': "Feature Toggles", 'icon': "fa-plug", 'authorities': "developer, oit-es-manager"},
        {'url': "psu:audit", 'label': "Audit Events", 'icon': "fa-id-card-o", 'authorities': "developer, oit-es-manager"},
        {'url': "psu:audit_xss", 'label': "XSS Attempts", 'icon': "fa-user-secret", 'authorities': "oit-es-manager"},
        {'url': "psu:finti", 'label': "Finti Interface", 'icon': "fa-laptop", 'authorities': "developer"},
        {'url': "psu:session", 'label': "Session Contents", 'icon': "fa-microchip", 'authorities': "developer"},
        {'url': "psu:email", 'label': "Send Test Email", 'icon': "fa-paper-plane-o", 'authorities': "developer"},
        {'url': "psu:scripts", 'label': "Admin Script", 'icon': "fa-code", 'authorities': "developer", 'feature': 'admin_script'},
    ]
}

# Finti test instance for Quick-start only.
# Only available on dev machines if "PSU Key" file is present
encryptor = Encryptor()
if encryptor.has_psu_key():
    FINTI_TOKEN = encryptor.decrypt(
        b'\xcb\xa0,m2\xcd\xee\xfe\x1f\x936\xdd/\x9b!\xb8\x8e\r\x92K\x93\xec\xa1\xd2p\xc9p\xfc\xa1L\xc2\x98\x87j\xc1\x9cF\x81\x96\xd0W\xbc\xd4\x97\xe8\xd0j\xa3+\xf0\xd1\xd7\xf8a_\xec7\xdeC\xc2C\x96\xac\x0f5}\x05\xf1\xd2]8\x0c\x05\xeb\xb6Py,\xc3N\x9e\x18\x85F*\x0e]q\x91HM\xc6\xe2O\x11\x0b\xe6;\xbc\t"\x7f\x83\xf8\xe3\xa2E\xdfJ\xa1:[n\xfc>\x132\xa3\x8f$\x11\x8fr\x17./\t8\xd6\xea\x9ce\xb8nc\\\xbc\xe4\xc2F\xf5\xf1\xf6F\x8d-\nc<6\xedpw/j\x92%\xb7\x90\x1f\x1e\xe6\x06\xb0\x95\r\xa3O=\xa0\xfc\x01h\xf7\x86\x9f\xe5\x89\xda\x08\x05\xf7\xfbs\x05\xef\xb5R\x8e\xec\xeb\xfb\xe8H\xd6`\x12N1ng\xce\x99\x9b[\xef!m\xdc\xe5\xee9\x94\xfa\xad\xf3\xbfl\xf6.\xcd\xe7\x97\xd0\x9bN|]t\xeb\xf2\xc6N\x0c\x10\xa9\xe8\xa8\x7fT\xe8\x18`>\xc9\xee5\x9b\x0e\xce5#\xa5\xb6&$\xd1*H\xde\x90C\n\x8e:2J\'2QQ\x8e\xe0Z(i_\xf7\x82\xf0I\xe3\x8d\x11pC[,(\xbe\x03\xfcO\x9b\x12\x1cn\x8a\xc6S\xa7\xff\x87\x1d\x0cj\x8ecL\x0fq\xb6\xb9B\xd0\xf5\r\x91\xf0\x94\xbc\xa5\xfe\x84t1\x0e+\xe0\xa1\x08"D\xbeH\x7f\xa7\x90\n\x97\xc6\xe1\x12<\n6:\x08\xe4\x1b\xcf\x9ba \xdb\x94S\xa5\xabdE\xf4\x839x\xeb8a\xbf<cx\xac\x81t\xac\x17\x1f\xf8\xf5\xf9#*j\x10\xd7r\x0fg\xc1H2\xfd\xa7\x19\x02\x9bl\x08w\x894P\x82\x95e\x95"\xea\x0ff=\xdb\x04&\x92\x15\xc1\x17\xf5\x81p\xdaxn\xe5\xc0\xaa<\xacY\xc3\xe0\xe8\x84`l\x8e\xaa\xdd%H\x0b\x07qR\x18aAS[\xcah\xeci\xb1\x87\xa8L\xfb\x06\xcf1\x03\xe1\xe7W-\xed\x83^<B:J\xba\xd5\xc3\x96\xa0\xe2\xe8\x91\xf5\xc5\x89\xb5?\xc1Dn\xc9WY@\xa4_{\xa6\xc7_g\x82\x0ci\xea\x8fN2y&\xd7')

# Assign default setting values
for key, value in _DEFAULTS.items():
    try:
        getattr(settings, key)
    except AttributeError:
        setattr(settings, key, value)
    # Suppress errors from DJANGO_SETTINGS_MODULE not being set
    except:
        pass
