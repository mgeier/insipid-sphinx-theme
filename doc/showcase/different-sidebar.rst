Page With Different Sidebar
===========================

This page has different content in the sidebar,
see :confval:`html_sidebars` in :download:`conf.py <../conf.py>`:

.. literalinclude:: ../conf.py
    :caption: conf.py
    :language: python
    :linenos:
    :lineno-match:
    :start-at: html_sidebars
    :end-at: }


Local Table of Contents
-----------------------

Instead of displaying the whole TOC in the sidebar
with ``globaltoc.html``,
a local TOC can be shown with ``localtoc.html``.


Search Box
----------

If you don't like the search button in the topbar,
you can also put a search field into the sidebar
by selecting the template ``searchbox.html``.

Like the search button, this is only available when JavaScript is enabled.
