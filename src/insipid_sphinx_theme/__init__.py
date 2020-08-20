"""An insipid Sphinx theme."""
from pathlib import Path

__version__ = '0.1.1'


def setup(app):
    """Sphinx extension entry point."""
    app.require_sphinx('1.6')  # For add_html_theme()
    app.add_html_theme('insipid', Path(__file__).resolve().parent / 'insipid')
    return {
        'version': __version__,
        'parallel_read_safe': True,
    }
