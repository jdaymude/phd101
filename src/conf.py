# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PHD 101'
author = 'Joshua J. Daymude'
copyright = '2022, ' + author

# The full version, including alpha/beta/rc tags
release = 'v0.0.0-alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_tabs.tabs',
    'sphinxcontrib.bibtex'
]

# Disable ability to close sphinx-tabs by clicking open tab.
sphinx_tabs_disable_tab_closing = True

# Configure sphinxcontrib-bibtex.
bibtex_bibfiles = ['ref.bib']
bibtex_reference_style = 'author_year'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/jdaymude/phd101",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "repository_branch": "main",
    "path_to_docs": "src/",
    "use_sidenotes": True,
    "extra_navbar": release
}
html_last_updated_fmt = ""

# The project's title, logo, and favicon.
html_title = project
# html_logo = "path/to/my/logo.png"
html_favicon = "_static/icon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
