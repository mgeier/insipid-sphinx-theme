"""An insipid Sphinx theme."""
from pathlib import Path

__version__ = '0.2.9'

def html_page_context(app, pagename, templatename, context, doctree):
    badge_css = 'https://assets.readthedocs.org/static/css/badge_only.css'
    try:
        app.builder.css_files.remove(badge_css)
    except ValueError:
        pass

def setup(app):
    """Sphinx extension entry point."""
    app.require_sphinx('1.6')  # For add_html_theme()
    app.add_html_theme('insipid', Path(__file__).resolve().parent / 'insipid')
    app.connect('html-page-context', html_page_context)
    return {
        'version': __version__,
        'parallel_read_safe': True,
    }
