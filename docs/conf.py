#!/usr/bin/env python3
#
# bluesky documentation build configuration file, created by
# sphinx-quickstart on Sun Jun  7 15:25:26 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

import requests

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "sphinxcontrib.mermaid",
]

# Configuration options for plot_directive. See:
# https://github.com/matplotlib/matplotlib/blob/f3ed922d935751e08494e5fb5311d3050a3b637b/lib/matplotlib/sphinxext/plot_directive.py#L81
plot_html_show_source_link = False
plot_html_show_formats = False
plot_pre_code = (
    "from matplotlib import pyplot as plt\n"
    "from bluesky import RunEngine\n"
    "from bluesky.callbacks.best_effort import BestEffortCallback\n"
    "RE = RunEngine({})\n"
    "bec = BestEffortCallback()\n"
    "RE.subscribe(bec)\n"
)

# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "bluesky"
copyright = "2015, Brookhaven National Lab"
author = "Brookhaven National Lab"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import bluesky  # noqa: E402

version = bluesky.__version__
# The full version, including alpha/beta/rc tags.
release = bluesky.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["src/bluesky/_vendor/"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
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

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
github_repo = project
github_user = "bluesky"
switcher_json = f"https://blueskyproject.io/{github_repo}/switcher.json"
switcher_exists = requests.get(switcher_json).ok
if not switcher_exists:
    print(
        "*** Can't read version switcher, is GitHub pages enabled? \n"
        "    Once Docs CI job has successfully run once, set the "
        "Github pages source branch to be 'gh-pages' at:\n"
        f"    https://github.com/{github_user}/{github_repo}/settings/pages",
        file=sys.stderr,
    )

# Theme options for pydata_sphinx_theme
# We don't check switcher because there are 3 possible states for a repo:
# 1. New project, docs are not published so there is no switcher
# 2. Existing project with latest copier template, switcher exists and works
# 3. Existing project with old copier template that makes broken switcher,
#    switcher exists but is broken
# Point 3 makes checking switcher difficult, because the updated copier template
# will fix the switcher at the end of the docs workflow, but never gets a chance
# to complete as the docs build warns and fails.
html_theme_options = {
    "logo": {
        "text": project,
    },
    "use_edit_page_button": True,
    "github_url": f"https://github.com/{github_user}/{github_repo}",
    "icon_links": [
        {
            "name": "PyPI",
            "url": f"https://pypi.org/project/{project}",
            "icon": "fas fa-cube",
        }
    ],
    "switcher": {
        "json_url": switcher_json,
        "version_match": version,
    },
    "check_switcher": False,
    "navbar_end": ["theme-switcher", "icon-links", "version-switcher"],
    # Ensure the toctrees created by autosummary directives are not visible in
    # left-panel navigation
    "navigation_depth": 1,
}

# # A dictionary of values to pass into the template engine’s context for all pages
html_context = {
    "github_user": github_user,
    "github_repo": github_repo,
    "github_version": version,
    "doc_path": "docs",
}

# # If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = False

# # If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = False

# # Logo
html_logo = "images/bluesky-logo-dark.svg"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "bluesky.tex", "bluesky Documentation", "Brookhaven National Lab", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "bluesky", "bluesky Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "bluesky",
        "bluesky Documentation",
        author,
        "bluesky",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "ophyd": ("https://blueskyproject.io/ophyd/", None),
    "event-model": ("https://blueskyproject.io/event-model/main", None),
}

sys.path.append(os.path.abspath("examples"))
