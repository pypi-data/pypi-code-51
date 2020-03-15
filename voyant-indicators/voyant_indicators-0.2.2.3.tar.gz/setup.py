#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["Click>=7.0","numpy", "pandas", "pykalman" ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Marmik Pandya",
    author_email='marmikapndya@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="technical analysis indicators for voyant",
    entry_points={
        'console_scripts': [
            'voyant_indicators=voyant_indicators.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='voyant_indicators',
    name='voyant_indicators',
    packages=find_packages(include=['voyant_indicators', 'voyant_indicators.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/marmikcfc/voyant_indicators',
    version='0.2.2.3',
    zip_safe=False,
)
