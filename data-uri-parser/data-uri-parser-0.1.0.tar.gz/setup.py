# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['data_uri_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'data-uri-parser',
    'version': '0.1.0',
    'description': 'A Pythonic data uri parser',
    'long_description': None,
    'author': 'Unmade',
    'author_email': 'backend@unmade.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
