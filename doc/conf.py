# Configuration file for Sphinx,
# see https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Recommended settings -----------------------------------------------------

html_theme = 'insipid'

html_permalinks_icon = '#'

# If False, source links to Bitbucket/Github/GitLab are shown (using html_context)
html_copy_source = False

# Update this with your own repo information:
html_context = {
    'display_github': True,
    'github_user': 'mgeier',
    'github_repo': 'insipid-sphinx-theme',
    'conf_py_path': '/doc/',
    'READTHEDOCS': os.environ.get('READTHEDOCS', False),
    # The 'commit' field is overwritten below (with data from Git).
    # If you prefer, you can also get it from your build environment,
    # e.g. READTHEDOCS_GIT_COMMIT_HASH.
    'commit': '???',
}

# -- Settings for source code -------------------------------------------------

# Language used for syntax highlighting (default: 'python')
#highlight_language = 'none'

# Style of syntax highlighting
#pygments_style = 'monokai'

# -- Language settings --------------------------------------------------------

#language = 'es'

# Date format used in footer. Use empty string for (language-specific) default.
# 'sphinx_last_updated_by_git' extension provides modification dates per page.
#html_last_updated_fmt = '%Y-%m-%d %H:%M:%S %Z'

# -- Theme configuration ------------------------------------------------------

html_theme_options = {
    #'body_centered': False,
    #'body_max_width': None,
    #'breadcrumbs': True,
    #'enable_search_shortcuts': False,
    #'globaltoc_collapse': False,
    #'globaltoc_includehidden': True,
    #'initial_sidebar_visibility_threshold': None,
    #'left_buttons': [
    #],
    #'navigation_with_keys': False,
    #'nosidebar': True,
    #'right_buttons': [
    #    'search-button.html',
    #],
    #'rightsidebar': True,
    #'show_insipid': False,
    #'sidebar_overlay_width': None,
    #'sidebar_transition': '1s ease-out',
    #'sidebarwidth': '10rem',
    #'strip_section_numbers': False,
    #'topbar_transition': '1.5s ease-out',
}

html_sidebars = {
   '**': [
       'github-badge.html',  # Custom template, see _templates/
       'home.html',
       'globaltoc.html',
       'separator.html',
       'indices.html',
   ],
   'showcase/different-sidebar': [
       'localtoc.html',
       'searchbox.html',
   ],
   'showcase/no-sidebar': [],
}

html_static_path = ['_static']
templates_path = ['_templates']

# -- Project information ------------------------------------------------------

project = 'insipid-sphinx-theme'
#html_title = 'Insipid Sphinx Theme'
html_short_title = 'insipid'
#copyright = '<insert year and copyright holder>'
#version = '3.14'
#release = '3.14.dev2'

html_logo = 'showcase/insipid.png'
html_favicon = '_static/favicon.svg'

# -- Page footer --------------------------------------------------------------

html_show_copyright = False
#html_show_sphinx = False
#html_show_sourcelink = False

# Only relevant when html_copy_source is True
#html_sourcelink_suffix = ''

# -- Miscellaneous settings ---------------------------------------------------

# Numbered figures, tables and code-blocks
numfig = True

html_secnumber_suffix = '\N{FIGURE SPACE}'

#html_compact_lists = False

#smartquotes = False

# Generate alphabetic index
#html_use_index = False

# Separate page per starting letter
#html_split_index = True

# Generate domain indices, e.g. Python module index
#html_domain_indices = False

# The default in Sphinx 4+ is 'inline'
#html_codeblock_linenos_style = 'table'

# -- Sphinx extensions --------------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_last_updated_by_git',
]

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/', None),
}

# -- Set path for example_module.py -------------------------------------------

# Normally, this is not necessary, because you should properly install
# your Python module before running Sphinx.

import os
import sys

sys.path.append(os.path.abspath('.'))

# -- Get version information from Git -----------------------------------------

try:
    from subprocess import check_output
    release = check_output(
        ['git', 'describe', '--tags', '--always']).decode().strip()
    html_context['commit'] = check_output(
        ['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
except Exception:
    release = '<unknown>'

# -- Define custom directives/roles -------------------------------------------


def gh_template_role(rolename, rawtext, text, lineno, inliner,
                     options={}, content=()):
    from docutils import nodes, utils
    github_url = 'https://github.com/mgeier/insipid-sphinx-theme'
    blob_url = github_url + '/blob/' + release
    base_url = blob_url + '/src/insipid_sphinx_theme/insipid/%s'
    text = utils.unescape(text)
    full_url = base_url % text
    pnode = nodes.reference(internal=False, refuri=full_url)
    pnode += nodes.literal(text, text, classes=['file'])
    return [pnode], []


def setup(app):
    app.add_object_type(
        'confval', 'confval',
        objname='Sphinx configuration value',
        indextemplate='pair: %s; Sphinx configuration value')
    app.add_object_type(
        'theme-option', 'theme-option',
        objname='Theme option',
        indextemplate='pair: %s; Theme option')
    app.add_role('gh-template', gh_template_role)
