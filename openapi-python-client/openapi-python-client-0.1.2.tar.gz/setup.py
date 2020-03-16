# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openapi_python_client', 'openapi_python_client.openapi_parser']

package_data = \
{'': ['*'], 'openapi_python_client': ['templates/*']}

install_requires = \
['click-completion>=0.5.2,<0.6.0',
 'jinja2>=2.11.1,<3.0.0',
 'requests>=2.22.0,<3.0.0',
 'stringcase>=1.2.0,<2.0.0',
 'typer>=0.0.8,<0.0.9']

extras_require = \
{':sys_platform == "win32"': ['colorama>=0.4.3,<0.5.0']}

entry_points = \
{'console_scripts': ['openapi-python-client = openapi_python_client.cli:app']}

setup_kwargs = {
    'name': 'openapi-python-client',
    'version': '0.1.2',
    'description': 'Generate modern Python clients from OpenAPI',
    'long_description': '[![triaxtec](https://circleci.com/gh/triaxtec/openapi-python-client.svg?style=svg)](https://circleci.com/gh/triaxtec/openapi-python-client)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![codecov](https://codecov.io/gh/triaxtec/openapi-python-client/branch/master/graph/badge.svg)](https://codecov.io/gh/triaxtec/openapi-python-client)\n[![PyPI version shields.io](https://img.shields.io/pypi/v/openapi-python-client.svg)](https://pypi.python.org/pypi/openapi-python-client/)\n\n# openapi-python-client\nGenerate modern Python clients from OpenAPI\n\n**This project is still in early development and does not support all OpenAPI features**\n\n## Why This?\nThe Python clients generated by openapi-generator support Python 2 and therefore come with a lot of baggage. This tool \naims to generate clients which:\n1. Use all the latest and greatest Python features like type annotations and dataclasses\n1. Don\'t carry around a bunch of compatibility code for older version of Python (e.g. the `six` package)\n1. Have better documentation and more obvious usage instructions\n\nAdditionally, because this generator is written in Python, it should be more accessible to contribution by the people \nusing it (Python developers).\n\n## Installation\n`pip install openapi-python-client`\n\nThen, if you want tab completion: `openapi-python-client --install-completion`\n\n## Usage\n### Create a new client\n`openapi-python-client generate --url https://my.api.com/openapi.json`\n\nThis will generate a new client library named based on the title in your OpenAPI spec.  For example, if the title \nof your API is "My API", the expected output will be "my-api-client".  If a folder already exists by that name, you\'ll \nget an error.\n\n### Update an existing client\n`openapi-python-client update --url https://my.api.com/openapi.json`\n\n## What You Get\n1. A `pyproject.toml` file with some basic metadata intended to be used with [Poetry].\n1. A `README.md` you\'ll most definitely need to update with your project\'s details\n1. A Python module named just like the auto-generated project name (e.g. "my_api_client") which contains:\n    1. A `client` module which will have both a `Client` class and an `AuthenticatedClient` class.  You\'ll need these \n    for calling the functions in the `api` module.\n    1. An `api` module which will contain one module for each tag in your OpenAPI spec, as well as a `default` module \n    for endpoints without a tag.  Each of these modules in turn contains one function for calling each endpoint.\n    1. A `models` module which has all the classes defined by the various schemas in your OpenAPI spec\n    \n## OpenAPI features supported\n1. All HTTP Methods\n1. JSON and form bodies, path and query parameters\n1. float, string, int, datetimes, string enums, and custom schemas or lists containing any of those\n1. html/text or application/json responses containing any of the previous types\n1. Bearer token security\n\n\n## Contributors \n - Dylan Anthony <danthony@triaxtec.com> (Owner)\n\n\n[CHANGELOG.md]: CHANGELOG.md\n[Poetry]: https://python-poetry.org/\n',
    'author': 'Dylan Anthony',
    'author_email': 'danthony@triaxtec.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
