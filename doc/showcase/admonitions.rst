.. tip::

    Admonitions can also be used before the first headline.

Admonitions
===========

Specific Admonitions
--------------------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#specific-admonitions

In many themes only ``note`` and ``warning`` are supported!

.. attention::

    Attention text and ``inline code``.

.. caution::

    Caution text and ``inline code``.

.. danger::

    Danger text and ``inline code``.

.. error::

    Error text and ``inline code``.

.. hint::

    Hint text and ``inline code``.

.. important::

    Important text and ``inline code``.

.. note::

    Note text and ``inline code``.

.. tip::

    Tip text and ``inline code``.

.. warning::

    Warning text and ``inline code``.


Generic Admonitions
-------------------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#generic-admonition

.. admonition:: Admonition title with :doc:`a link <admonitions>` and ``code``

    Admonition text with :doc:`a link <admonitions>` and ``code``.


.. _topic:

Topic
-----

https://docutils.sourceforge.io/docs/ref/rst/directives.html#topic

.. topic:: Topic title with :doc:`a link <admonitions>` and ``code``

    Topic text and ``inline code``.


.. _sidebar:

Sidebar
-------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#sidebar

.. sidebar:: Sidebar Title with :doc:`a link <admonitions>` and ``code``
    :subtitle: Sidebar Subtitle

    ``sidebar`` text.

Text after first ``sidebar`` directive.

.. sidebar:: Second Sidebar

    More text.

Text after second ``sidebar`` directive.

    Block quote after sidebar.

    --Anonymous

.. sidebar:: Another Sidebar

    Text.

.. note::

    Note after ``sidebar``.

.. sidebar:: Yet Another Sidebar

    Text.

.. topic:: Topic after ``sidebar``.

    Text.

.. sidebar:: One More Sidebar

    Text.

.. warning::

    Warning after ``sidebar``.

.. sidebar:: And Another Sidebar

    Text.

.. seealso:: ``seealso`` after ``sidebar``


Admonition-like Constructs
--------------------------

https://www.sphinx-doc.org/en/master/extdev/nodes.html#new-admonition-like-constructs

.. seealso:: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-seealso
    and ``some inline code``

.. seealso::

    Text.

    Module :mod:`insipid_sphinx_theme`
        Documentation of the :mod:`insipid_sphinx_theme` module.

    `Sphinx Documentation <https://www.sphinx-doc.org/>`_
        Documentation for Sphinx.

.. versionadded:: 3.14

    https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionadded

.. versionchanged:: 3.14

    https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionchanged

.. deprecated:: 3.14

    https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-deprecated


Nesting
-------

.. note::

    .. warning::

        This is a warning.

        .. note::

            Inner note text.

        This is the warning again.


.. topic:: Topic

    .. note::

        Topic within admonition is not allowed!
        Topic within topic neither!

.. topic:: Topic

    .. warning::

        Deep nesting ahead:

        .. seealso::

            Note
                .. note::

                    You shouldn't use such deep nesting.

            Warning
                .. warning::

                    Really!

.. topic:: Topic

    .. seealso::

        Text.

.. sidebar:: Sidebar

    .. note::

        Note in sidebar.

.. sidebar:: Sidebar

    .. topic:: Topic

        Topic in sidebar.

.. seealso::

    .. note::

        Note text.

..

    .. note::

        Admonition in a block quote.


Overflow
--------

.. admonition:: A long long long long long long long long long long long long
    long long long long long long long long long long long long long long long
    admonition title

    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

.. topic:: A long long long long long long long long long long long long
    long long long long long long long long long long long long long long long
    topic title

    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

.. sidebar:: A long long long long long long long long long long long long
    long long long long long long long long long long long long long long long
    sidebar title

    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
    = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
