#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################################
#                                                                                 #
# Copyright (c) 2019 Idiap Research Institute, http://www.idiap.ch/               #
# Contact: beat.support@idiap.ch                                                  #
#                                                                                 #
# Redistribution and use in source and binary forms, with or without              #
# modification, are permitted provided that the following conditions are met:     #
#                                                                                 #
# 1. Redistributions of source code must retain the above copyright notice, this  #
# list of conditions and the following disclaimer.                                #
#                                                                                 #
# 2. Redistributions in binary form must reproduce the above copyright notice,    #
# this list of conditions and the following disclaimer in the documentation       #
# and/or other materials provided with the distribution.                          #
#                                                                                 #
# 3. Neither the name of the copyright holder nor the names of its contributors   #
# may be used to endorse or promote products derived from this software without   #
# specific prior written permission.                                              #
#                                                                                 #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED   #
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE          #
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL      #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR      #
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER      #
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,   #
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE   #
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.            #
#                                                                                 #
###################################################################################


import time
import os
import pkg_resources
import sphinx_rtd_theme

# For inter-documentation mapping:
from bob.extension.utils import link_documentation, load_requirements

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.3"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
]

# Be picky about warnings
nitpicky = True

# Ignores stuff we can't easily resolve on other project's sphinx manuals
nitpick_ignore = []

# Allows the user to override warnings from a separate file
if os.path.exists("nitpick-exceptions.txt"):
    for line in open("nitpick-exceptions.txt"):
        if line.strip() == "" or line.startswith("#"):
            continue
        dtype, target = line.split(None, 1)
        target = target.strip()
        try:  # python 2.x
            target = unicode(target)
        except NameError:
            pass
        nitpick_ignore.append((dtype, target))

# Always includes todos
todo_include_todos = True

# Generates auto-summary automatically
autosummary_generate = True

# Create numbers on figures with captions
numfig = True

# If we are on OSX, the 'dvipng' path maybe different
dvipng_osx = "/Library/TeX/texbin/dvipng"
if os.path.exists(dvipng_osx):
    pngmath_dvipng = dvipng_osx

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"beat.core"

copyright = u"%s, Idiap Research Institute" % time.strftime("%Y")

# Grab the setup entry
distribution = pkg_resources.require(project)[0]

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = distribution.version
# The full version, including alpha/beta/rc tags.
release = distribution.version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["links.rst"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# Some variables which are useful for generated material
project_variable = project.replace(".", "_")
short_description = u"Core modules and definitions for the BEAT platform"
owner = [u"Idiap Research Institute"]


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = project_variable

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "img/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = project_variable + u"_doc"


# -- Post configuration --------------------------------------------------------

# Included after all input documents
rst_epilog = """
.. |project| replace:: BEAT
.. |version| replace:: %s
.. |current-year| date:: %%Y
""" % (
    version,
)

# Default processing flags for sphinx
autoclass_content = "class"
autodoc_member_order = "bysource"
autodoc_default_flags = ["members", "undoc-members", "show-inheritance"]

if "BOB_DOCUMENTATION_SERVER" not in os.environ:
    # notice we need to overwrite this for BEAT projects - defaults from Bob are
    # not OK
    os.environ[
        "BOB_DOCUMENTATION_SERVER"
    ] = "https://www.idiap.ch/software/beat/docs/beat/%(name)s/%(version)s/|https://www.idiap.ch/software/beat/docs/beat/%(name)s/master/"

sphinx_requirements = "extra-intersphinx.txt"
if os.path.exists(sphinx_requirements):
    intersphinx_mapping = link_documentation(
        additional_packages=["python", "numpy"] + load_requirements(sphinx_requirements)
    )
else:
    intersphinx_mapping = link_documentation()

# Adds simplejson, pyzmq links
intersphinx_mapping["http://simplejson.readthedocs.io/en/stable/"] = None
intersphinx_mapping["http://pyzmq.readthedocs.io/en/stable/"] = None
intersphinx_mapping["http://python-jsonschema.readthedocs.io/en/stable/"] = None
intersphinx_mapping["https://docker-py.readthedocs.io/en/stable/"] = None

# We want to remove all private (i.e. _. or __.__) members
# that are not in the list of accepted functions
accepted_private_functions = ["__array__"]


def member_function_test(app, what, name, obj, skip, options):
    # test if we have a private function
    if len(name) > 1 and name[0] == "_":
        # test if this private function should be allowed
        if name not in accepted_private_functions:
            # omit private functions that are not in the list of accepted private
            # functions
            return skip
        else:
            # test if the method is documented
            if not hasattr(obj, "__doc__") or not obj.__doc__:
                return skip
    return False


def setup(app):
    app.connect("autodoc-skip-member", member_function_test)
