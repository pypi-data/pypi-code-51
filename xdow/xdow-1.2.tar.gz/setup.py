from setuptools import setup
long_description = ''
with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='xdow',
    version='1.2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Adult video downloader',
    author='pankaj kumar',
    author_email='pankajthekush@gmail.com',
    packages=['xdow'],
    install_requires=['js2py', 'requests', 'bs4','wheel'],
    entry_points={"console_scripts": ["xdow = xdow.xdow:classifier"]}
)
