from setuptools import setup,find_packages
setup(name='pylink_core',
      version='0.5',
      description='a small example',
      classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
      url='https://www.python.org/',
      author='zhushaodong123',
      author_email='',
      license='NEU',
      packages=find_packages(),
      package_data={"":["*.pyc"]},
      zip_safe=True
     )

