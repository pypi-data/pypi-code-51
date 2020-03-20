# Environment choices: {DEV, TEST, PROD}
ENVIRONMENT = 'DEV'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3c4zcw#^0jq7s$^@uw_#ej_n0!t1q*x*gmmf9nr$^x6$2u49sl'

# Name of machine running the application
ALLOWED_HOSTS = ['localhost']

# Debug mode (probably only true in DEV)
DEBUG = True

# SSO URL
CAS_SERVER_URL = 'https://sso-stage.oit.pdx.edu/idp/profile/cas/login'

# Finti URL (dev, test, or prod)
FINTI_TOKEN = '0b689a3a-dbef-32a0-c953-3d4aff240f6d'
FINTI_URL = 'https://ws-test.oit.pdx.edu'

# Finti URLs (for reference)
# http://localhost:8888
# https://ws-test.oit.pdx.edu
# https://ws.oit.pdx.edu

FINTI_SIMULATE_CALLS = True    # Simulate Finti calls (i.e. when not on VPN)
FINTI_SAVE_RESPONSES = True    # Save/record actual Finti responses for offline use?

ELEVATE_DEVELOPER_ACCESS = True

# Session expiration
SESSION_COOKIE_AGE = 4 * 60 * 60  # 4 hours
