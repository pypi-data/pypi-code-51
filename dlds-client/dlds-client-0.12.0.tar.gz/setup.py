#  Copyright (c) 2019 Data Spree UG (haftungsbeschraenkt) - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited.
#  Proprietary and confidential.

from setuptools import setup

setup(
    name='dlds-client',
    version='0.12.0',
    author="Eric Dörheit",
    author_email="eric.doerheit@data-spree.com",
    description="Python API for Deep Learning DS from Data Spree.",
    packages=[
        'dlds.decoder'
    ],
    py_modules=[
        'dlds.dlds_cli',
        'dlds.dlds_client',
        'dlds.dlds_data_loader',
        'dlds.dlds_model',
        'dlds.dlds_worker',
        'dlds.http_token_authentication'
    ],
    install_requires=[
        'aiohttp',
        'Click',
        'joblib',
        'numpy',
        'Pillow',
        'requests',
        'tqdm',
    ],
    entry_points='''
        [console_scripts]
        dlds=dlds_cli:cli
    ''',
    python_requires='>=3.6'
)
