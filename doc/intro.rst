Introduction
============

This Sphinx_ theme was very much inspired by (i.o.w. ripped off of) mdBook_.

Some further ideas were stolen from the Sphinx themes
sphinx_typlog_theme_ (https://readthedocs.org/ badge),
sphinx_material_ (previous/next arrows in relbar),
sphinx_book_theme_ (fullscreen button),
furo_ (sidebar that can be toggled without JavaScript),
as well as websites like
Github_,
MDN_,
and many others.

If you don't like this theme, no problem,
Sphinx has several :ref:`builtin-themes` to choose from and
you can find a large list of third-party Sphinx themes at
https://sphinx-themes.org/.
You can also search for Sphinx themes on PyPI__, GitLab__ and Github__.

__ https://pypi.org/search/?c=Framework+::+Sphinx+::+Theme
__ https://gitlab.com/explore?name=sphinx+theme
__ https://github.com/search?q=sphinx+theme

.. _Sphinx: https://www.sphinx-doc.org/
.. _mdBook: https://rust-lang.github.io/mdBook/
.. _sphinx_typlog_theme: https://sphinx-typlog-theme.readthedocs.io/
.. _sphinx_material: https://bashtage.github.io/sphinx-material/
.. _sphinx_book_theme: https://sphinx-book-theme.readthedocs.io/
.. _furo: https://pradyunsg.me/furo/quickstart/
.. _Github: https://github.com/
.. _MDN: https://developer.mozilla.org/en-US/docs/Web


Goals
-----

The following list has been driving the development of this theme.
Those are the *goals*, but that doesn't necessarily mean that any of them has
been reached (to a sufficient degree) yet.

If you have suggestions how to come closer to these goals,
please create an issue or -- even better! -- a pull request
at https://github.com/mgeier/insipid-sphinx-theme/.

boring
    The most important thing is your content.
    It shouldn't be outshined by some flashy theme.
    The theme is supposed to stay in the background and out of the way.

    This theme uses only very few (and only locally available) fonts,
    very few (and quite dull) colors
    and just a handful of simple symbols.

    Most navigational tools can be hidden (and are in fact hidden by default),
    providing a maximum of screen real estate for
    and a minimum of distraction from your content.
    Only if your browser window is extremely wide, the sidebar will be shown
    on the initial visit.  This can be configured with
    :theme-option:`initial_sidebar_visibility_threshold`.

accessible
    *Help needed!*
    There are some ``aria-label``\s here and there,
    but the accessibility could certainly be improved in many places.

mobile-friendly
    This theme should work well on (reasonably modern) mobile devices.
    Considerable care has been taken to make sure all the screen space is
    available for content and not obstructed by ornamental junk.

configurable
    The default settings should be perfectly fine for most people.
    But doesn't everyone sometimes like to be special?
    Many features can be switched on and off (see :doc:`configuration`),
    and thanks to Sphinx's great flexibility,
    you can fine-tune and individualize virtually every aspect of the theme,
    see :doc:`customization` for details.

support for right-to-left languages
    *Help needed!*
    For now, there are no special arrangements in place
    except for a measly :theme-option:`rightsidebar` theme option.

optional JavaScript
    Some features (like resizing the sidebar, storing the sidebar state when
    navigating between pages, hiding/showing the topbar, search,
    fullscreen button) require JavaScript.
    However, if JavaScript is disabled,
    all content should still be perfectly readable and the navigation within
    and between pages should still work well.
    Even opening and closing the sidebar works without JavaScript.

support for *all* Sphinx features
    The largest part of this documentation
    (starting at :doc:`showcase/index`)
    is a showcase of (hopefully) all
    things that can be generated with Sphinx (aside from arbitrary "raw" HTML).
    If you find something that isn't supported (or not shown in the docs),
    please let us know!

back to the ``basic``\s
    This theme is derived from Sphinx's ``basic`` theme
    and only adds some hand-written HTML, CSS and JavaScript
    (sprinkled with a pinch of Jinja2_ markup).
    Plus a few SVG icons from `Font Awesome`_
    (embedded in the HTML files -- no external assets).
    No external JavaScript framework is used
    (except for jQuery_ and underscore.js_,
    which are already part of the ``basic`` theme),
    and no extension-specific Python code is ever executed
    (you can check the source code of :func:`insipid_sphinx_theme.setup`).

    .. _Jinja2: https://palletsprojects.com/p/jinja/
    .. _Font Awesome: https://fontawesome.com/
    .. _jQuery: https://jquery.com/
    .. _underscore.js: https://underscorejs.org/


Features
--------

First of all, the ``insipid`` theme tries to not disable any features
that Sphinx (and its ``basic`` theme, see :ref:`basic settings`) already has.

Here's a little selection of features, some of them provided by Sphinx itself,
some added by the ``insipid`` theme:

auto-hiding topbar
    The goal is to maximize (vertical) screen space and to get out of the way.
    Therefore, the topbar disappears when scrolling down.
    When scrolling up,
    or when hovering over (or touching) the top part of the screen,
    it re-appears.

    The topbar contains some useful icons
    (see :theme-option:`left_buttons` and :theme-option:`right_buttons`)
    as well as the title of the current page.
    When clicking on said title, the page is scrolled to the top
    and the title of the parent document is displayed.
    Clicking on that brings you to the parent document.

resizable sidebar
    In addition to toggling its visibility,
    the width of the sidebar can also be interactively changed by users.
    The new width (and whether the sidebar is visible or not)
    is stored in the browser's "local storage",
    which means it will be remembered for the next visit.

    The default width can be configured with the theme option
    :theme-option:`sidebarwidth`,
    the content of the sidebar can be configured with
    :confval:`html_sidebars` (and :confval:`html_logo`).

    On devices with a touchscreen,
    the sidebar can be opened/closed with a swipe right/left gesture.

keyboard navigation
    This is one of the features that's provided by Sphinx,
    but several third-party themes have inadvertently disabled it.

    You can switch between pages using the left and right arrow keys.
    This feature can be disabled with :theme-option:`navigation_with_keys`.

    In addition to the left/right arrow keys,
    several key combinations are provided using the ``accesskey`` HTML feature.
    The way to use these keyboard shortcuts depends on the browser
    and the operating system, typically involving holding the :kbd:`Alt` key,
    often combined with the :kbd:`Shift` or the :kbd:`Control` key.
    For details, see e.g. MDN__.

    __ https://developer.mozilla.org/en-US/docs/
        Web/HTML/Global_attributes/accesskey

    The following access keys are available in many Sphinx themes:
    :kbd:`N` for the *next* page;
    :kbd:`P` for the *previous* page;
    :kbd:`U` for *up* (to the parent page);
    :kbd:`I` for the *index*.
    In addition to these, the ``insipid`` theme provides
    :kbd:`S` to show/hide the *search* field and
    :kbd:`M` for showing/hiding the sidebar (i.e. the *menu*).

fullscreen mode
    When supported by the browser
    (and when not overridden with :theme-option:`right_buttons`),
    the topbar contains an icon for switching into (and out of)
    fullscreen mode.

    Navigating to another page will typically exit fullscreen mode.

translatable UI
    All strings used in the user interface (including ``aria-label``\s)
    are translatable and
    they will be automatically replaced by their translations
    when a supported :confval:`language` setting is used.

support for https://readthedocs.org/
    The RTD "badge" (for selecting versions, languages etc.)
    is incorporated into the bottom of the ``insipid`` sidebar
    (instead of floating around in the bottom right corner of the page).

    Furthermore, a link to the connected Bitbucket/Github/GitLab repository
    is automatically displayed in the topbar.
    This can be disabled by overriding :theme-option:`right_buttons`.

    Finally, if :confval:`html_copy_source` is set to ``False``,
    a "show source" link to the appropriate version of the page source
    on Bitbucket/Github/GitLab is shown in the footer of each page.
    The link can be disabled by setting
    :confval:`html_show_sourcelink` to False.
