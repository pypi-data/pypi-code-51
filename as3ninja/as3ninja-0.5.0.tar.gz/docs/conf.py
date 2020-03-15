# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import as3ninja

# -- Project information -----------------------------------------------------

project = as3ninja.__projectname__
copyright = '2019, ' + as3ninja.__author__
author = as3ninja.__author__

# The full version, including alpha/beta/rc tags
release = as3ninja.__version__
# The short X.Y version.
version = as3ninja.__version__
# The full version, including alpha/beta/rc tags.
release = as3ninja.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.todo',
        'sphinx.ext.viewcode',
        'sphinx.ext.autodoc',
        'sphinx_autodoc_typehints',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# enable todos
todo_include_todos = True

# autodoc settings
autodoc_default_options = {
    'private-members': True,
    'undoc-members': True,
    'ignore-module-all': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
