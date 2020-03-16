from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='tobiiglasses',
    version='0.9',
    description='An open-source Python suite for Tobii Pro Glasses 2',
    url='https://github.com/ddetommaso/TobiiGlassesPySuite',
    download_url='https://github.com/ddetommaso/TobiiGlassesPySuite/archive/0.9.tar.gz',
    install_requires=['tobiiglassesctrl>=2.2.5', 'tornado', 'nose', 'pandas', 'opencv-python>=4.2.0.32', 'opencv-contrib-python>=4.2.0.32', 'sortedcontainers==1.5.10', 'dlib'],
    author='Davide De Tommaso',
    author_email='dtmdvd@gmail.com',
    keywords=['eye-tracker','tobii','glasses', 'tobii pro glasses 2', 'tobii glasses', 'eye tracking'],
    packages=find_packages(exclude=['examples*']),
    package_data={'tobiiglasses.aoi.dnn.faces': ['data/*.*']},
    include_package_data=True,
    classifiers = [
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
    ],
)
