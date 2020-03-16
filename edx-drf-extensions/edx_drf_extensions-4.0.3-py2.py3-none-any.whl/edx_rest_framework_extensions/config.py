"""
Application configuration constants and code.
"""

# .. toggle_name: EDX_DRF_EXTENSIONS[ENABLE_SET_REQUEST_USER_FOR_JWT_COOKIE]
# .. toggle_implementation: DjangoSetting
# .. toggle_default: False
# .. toggle_description: Toggle for setting request.user with jwt cookie authentication
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release
# .. toggle_creation_date: 2019-10-15
# .. toggle_expiration_date: 2019-12-31
# .. toggle_warnings: This feature fixed ecommerce, but broke edx-platform. The toggle enables us to fix over time.
# .. toggle_tickets: ARCH-1210, ARCH-1199, ARCH-1197
# .. toggle_status: supported
ENABLE_SET_REQUEST_USER_FOR_JWT_COOKIE = 'ENABLE_SET_REQUEST_USER_FOR_JWT_COOKIE'
