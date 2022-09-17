Configuration
=============

If you want to use the ``insipid`` theme,
only a single setting is required in your :file:`conf.py`:

.. code-block:: python

    html_theme = 'insipid'

However, you may also want to change the default symbol for section title links
from the default ¶ to something more meaningful like # or § or maybe 🔗:

.. code-block:: python

    html_permalinks_icon = '#'

And if you happen to host your documentation on https://readthedocs.org/
and your sources on Bitbucket, Github or GitLab, you should set:

.. code-block:: python

    html_copy_source = False

This way, you will get automatic source links in the page footer.
See :confval:`html_show_sourcelink` for details.


Theme Settings
--------------

The ``insipid`` theme has many configuration parameters
which can be specified with :confval:`html_theme_options`
in your :file:`conf.py`,
for example like this:

.. code-block:: python
    :caption: A simple :file:`conf.py`
    :name: conf-py-simple

    html_theme = 'insipid'
    html_theme_options = {
        'body_centered': False,
        'breadcrumbs': True,
    }

You can also have a look at the `example`_ below.

All available theme options are listed in the following sections.


``insipid`` Settings
^^^^^^^^^^^^^^^^^^^^

The following settings are provided by the ``insipid`` theme.
See below for `default values`_.

.. theme-option:: body_centered

    Set to ``False`` if you want the body text to be left-aligned.

    If :theme-option:`body_max_width` is ``None``, this has no effect.

.. theme-option:: breadcrumbs

    Set to ``True`` to show breadcrumb navigation
    (including a "home" button)
    at the top of each page
    (via the :gh-template:`page.html` template).

.. theme-option:: initial_sidebar_visibility_threshold

    The visibility of the sidebar depends on the setting from the previous
    visit, which is stored in the browser's ``localStorage``.
    If no information is available (i.e., on the first visit),
    the sidebar is hidden, except if the browser window is wider
    than the given threshold (in pixels or any CSS unit).
    If ``None`` is given, or if JavaScript is disabled in the browser,
    the sidebar is initially hidden, regardless of screen width.

.. theme-option:: left_buttons

    List of templates to show on the left side of the title bar.

    You can use one of the built-in templates
    (ending with :file:`-button.html`):

    :gh-template:`search-button.html`
        A button to show/hide the search field.

        .. note::

            This is only shown if :confval:`html_sidebars`
            does *not* contain ``'searchbox.html'``.

    :gh-template:`fullscreen-button.html`
        A button to switch to fullscreen mode (and back again).

        .. note::

            This will only be shown if fullscreen mode is available.

    :gh-template:`repo-button.html`
        A Bitbucket/Gitlab/Github logo linking to the associated repository.

        .. note::

            If your docs are hosted on https://readthedocs.org/
            this should work automagically.
            If not, you'll have to provide some information
            via :confval:`html_context`::

                html_context = {
                    'display_gitlab': True,
                    'gitlab_user': 'myuser',
                    'gitlab_repo': 'myrepo',
                }

            Replace ``gitlab`` with ``bitbucket`` or ``github``
            if the repository containing your source files is
            hosted on Bitbucket or Github, respectively.

    :gh-template:`pdf-button.html`
        A link to the PDF version of your docs.

        .. note::

            If your docs are hosted on https://readthedocs.org/
            (and if you've enabled PDF builds)
            this should work automagically.
            If not, you'll have to provide the URL to the PDF file
            via :confval:`html_context`::

                html_context = {
                    'downloads': [
                        ('pdf', 'https://example.org/my-docs.pdf'),
                    ],
                }

    You can also create your own template file(s) located in your
    :confval:`templates_path`.
    It's best to use ``<a>`` or ``<button type="button">`` elements.
    You can ``include`` other templates, most notably icons.

    For example, a "home" button could be made by creating a file
    named :file:`_templates/home-button.html`
    (relative to your :file:`conf.py`) with this content:

    .. code-block:: html+jinja

        <a href="{{ pathto('index') }}" title="{{ docstitle|e }}">
          {% include 'icons/home.svg' %}
        </a>

    ... and adding the file name to :confval:`html_theme_options`
    like this:

    .. code-block:: python

        html_theme_options = {
            'left_buttons': [
                'home-button.html',
            ],
        }
        templates_path = ['_templates']

    For help creating your own templates, see :doc:`sphinx:templating`.

.. theme-option:: right_buttons

    List of templates to show on the right side of the title bar.

    .. seealso:: :theme-option:`left_buttons`

.. theme-option:: rightsidebar

    Set to ``True`` if you want to move the sidebar from the left to the right.

    .. seealso:: :theme-option:`nosidebar`, :confval:`html_sidebars`

.. theme-option:: show_insipid

    Set to ``False`` to hide the "Insipid Theme" link in the footer.

.. theme-option:: sidebar_overlay_width

    When the browser window is narrower than this value
    (in pixels or any CSS unit) -- e.g. on a small mobile device --
    the sidebar will (partially) cover the main text.
    Set to ``None`` to disable.

.. theme-option:: sidebar_transition

    Duration (and optional timing function) of the CSS transition effect
    for showing/hiding the sidebar.

.. theme-option:: strip_section_numbers

    Section numbers (if you use them at all) are by default removed from
    previous/next links and from the title bar.
    Set to ``False`` to show them.

.. theme-option:: topbar_transition

    Duration (and optional timing function) of the CSS transition effect
    for showing/hiding the title bar.


.. _basic settings:

``basic`` Settings
^^^^^^^^^^^^^^^^^^

The following settings are inherited from the basic__ theme
(therefore, most Sphinx themes have them),
but for some of the options, the `default values`_ have been changed.

__ https://github.com/sphinx-doc/sphinx/blob/master/
    sphinx/themes/basic/theme.conf


.. theme-option:: body_max_width
    
    Maximal width of the main document text (in pixels or any CSS unit).
    Set it to ``None`` for unlimited width.

.. theme-option:: body_min_width

    Minimal width of the main document text (in pixels or any CSS unit).

.. theme-option:: globaltoc_collapse

    If ``True`` (the default), only the current section of the table of contents
    (TOC) in the sidebar is expanded.
    Set to ``False`` to expand everything.

.. theme-option:: globaltoc_includehidden

    If ``True``, include sections from :rst:dir:`toctree` directives
    with the ``:hidden:`` flag in the table of contents (TOC) in the sidebar.
    By default, hidden sections are not included.

.. theme-option:: navigation_with_keys

    If ``True``, the left and right arrow keys can be used to turn pages.

    .. note::
        This is disabled by default in the ``basic`` theme
        (and therefore in most other themes as well),
        for reasons given in Sphinx PR `#2064`__.

        __ https://github.com/sphinx-doc/sphinx/pull/2064

        When using the ``insipid`` theme, however, this is enabled by default.

.. theme-option:: nosidebar

    Set to ``True`` to completely disable the sidebar.

    .. seealso:: :theme-option:`rightsidebar`, :confval:`html_sidebars`

.. theme-option:: sidebarwidth

    Width of the sidebar (in pixels or any CSS unit).

    .. note::

        Whenever the sidebar is resized,
        its new width is stored in the browser's "local storage".
        Therefore, a changed ``sidebarwidth`` might not be immediately visible.


Default Values
^^^^^^^^^^^^^^

For default values, see:

.. literalinclude:: ../src/insipid_sphinx_theme/insipid/theme.conf
    :name: theme-conf
    :caption: :file:`insipid/theme.conf`
    :linenos:
    :language: ini


Sphinx Settings
---------------

Sphinx has *a lot* of settings --
read :doc:`the docs <sphinx:usage/configuration>`!
Here we only show a small selection of configuration values
which are relevant for the ``insipid`` theme.

.. confval:: html_copy_source

    When :confval:`sphinx:html_copy_source` is ``True``
    (which is the default),
    all source files are copied to the HTML output directory
    (into the :file:`_sources` sub-directory).
    The string given by :confval:`html_sourcelink_suffix`
    is appended to each file name.

    .. note::

        This has to be set to ``False`` in order to show links
        to the source files on Bitbucket/Gitlab/Github,
        see :confval:`html_show_sourcelink`.

.. confval:: html_show_sourcelink

    When :confval:`sphinx:html_show_sourcelink` is ``True``
    (which is the default),
    a link to the source file of each page is shown in the footer.

    Traditionally, those links point to copies of the source files
    (when :confval:`html_copy_source` has its default value ``True``).

    However, when :confval:`html_copy_source` is ``False``,
    the ``insipid`` theme (via the :gh-template:`show-source.html` template)
    will show links to the appropriate version of the source files on
    Bitbucket/Gitlab/Github.

    .. note::

        This should work automagically if your docs are hosted
        on https://readthedocs.org/.
        If not, you have to manually provide the necessary information
        via :confval:`html_context`::

            html_context = {
                'display_gitlab': True,
                'gitlab_user': 'myuser',
                'gitlab_repo': 'myrepo',
                'conf_py_path': '/path/to/doc/',
                'commit': '123abc',
            }

        The example above shows settings for Gitlab.
        Replace ``gitlab`` with ``bitbucket`` or ``github``
        if the repository containing your source files is
        hosted on Bitbucket or Github, respectively.

        The ``commit`` value should contain the hash (or tag name)
        of the commit which was used to create the docs.

.. confval:: html_sidebars

    The content of the sidebar consists of the :confval:`html_logo`
    (if specified), followed by the list of templates in
    :confval:`sphinx:html_sidebars`.

    You can choose from templates provided by the ``basic`` theme,
    like
    :file:`globaltoc.html`,
    :file:`localtoc.html`,
    :file:`relations.html`,
    :file:`searchbox.html` and
    :file:`sourcelink.html`.

    You can also select templates from the ``insipid`` theme:
    :gh-template:`home.html`,
    :gh-template:`indices.html` and
    :gh-template:`separator.html`.

    Finally, you can create your own custom templates.
    It's best to use ``<h3>``, ``<h4>`` and ``<p class="caption">`` elements
    for titles, as well as "normal" ``<p>`` and ``<ul>``
    (containing ``<li>`` elements which themselves typically
    contain ``<a href="...">`` links).
    To distinguish between internal and external links, you can use
    ``<a class="reference internal" ...>`` and
    ``<a class="reference external" ...>``, respectively.

    .. seealso:: Theme options :theme-option:`rightsidebar` and
        :theme-option:`nosidebar`

.. confval:: html_theme_options

    The value :confval:`sphinx:html_theme_options` contains all custom
    `theme settings`_.

.. confval:: language

    When a supported :confval:`sphinx:language` is chosen, all UI strings will
    be translated accordingly.


Example
-------

You can look at the :file:`conf.py` file of this very documentation:

.. literalinclude:: conf.py
    :name: conf-py
    :caption: :file:`conf.py` of the ``insipid`` docs
    :linenos:
    :language: python
    :end-before: Get version information from Git
