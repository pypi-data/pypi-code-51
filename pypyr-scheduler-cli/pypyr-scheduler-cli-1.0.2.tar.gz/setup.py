from setuptools import (setup, find_namespace_packages)
from os import path
from pkg_resources import parse_version

NAME = "pypyr-scheduler-cli"
VERSION = str(parse_version("1.0.2"))

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Command line Interface for pypyr-scheduler-server",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=f"https://github.com/pypyr-scheduler/{NAME}",
    license='MIT',

    author='David Zerrenner',
    author_email="dazer017@gmail.com",

    classifiers=[
                 'Intended Audience :: Developers',
                 "License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.7",
    ],

    keywords=["Pypyr", "Scheduler", "Taskrunner"],

    packages=find_namespace_packages(include=['pyrsched.*', ]),
    namespace_packages=['pyrsched'],
    include_package_data=True,
    # data_files=[
    #     ('conf', ['conf/scheduler_config.py',]),
    # ],

    install_requires=[
        "pypyr-scheduler-rpc-client",
        "rich",
        "halo",
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
