import os
import sys
import subprocess
from datetime import date

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
# import os
# import sys
sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

cdi = subprocess.check_output(["git", "--no-pager", "show", "-s", "--format='%h (%ci)'"]).strip().decode('utf-8').replace("'","")
project = "SC23 Workshop: High Performance Python for Science at Scale"
author = "Organizing Committee"
copyright = f"{date.today().year}, {author} - {cdi}"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "breathe",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

# autodoc_typehints = 'description'
autodoc_typehints_format = "short"
autodoc_class_signature = "separated"
autodoc_member_order = "bysource"
autosummary_generate = True

default_role = "any"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
tls_verify = False
html_show_sourcelink = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "_env", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Paths relative to html_static_path
html_css_files = [
    "css/custom.css",
]

# See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {}

add_module_names = False
