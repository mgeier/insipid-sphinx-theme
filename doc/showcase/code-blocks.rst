``Code`` Blocks
===============

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples


Literal Blocks
--------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks


This is a code sample::

    print('Hello, world!')


Quoted Literal Blocks
---------------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quoted-literal-blocks

Supported initial characters:
``! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~``::

! every line
! must
! start with the same character


``code-block`` Directive
------------------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block

.. code-block:: python
    :name: code1

    print('Hello,')
    print('wooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooorld!')

.. code-block:: python

    # another code block

No language:

.. code-block:: none

    ┌─┬┐  ╔═╦╗  ╓─╥╖  ╒═╤╕
    │ ││  ║ ║║  ║ ║║  │ ││
    ├─┼┤  ╠═╬╣  ╟─╫╢  ╞═╪╡
    └─┴┘  ╚═╩╝  ╙─╨╜  ╘═╧╛
    ┌───────────────────┐
    │  ╔═══╗ Some Text  │▒
    │  ╚═╦═╝ in the box │▒
    ╞═╤══╩══╤═══════════╡▒
    │ ├──┬──┤           │▒
    │ └──┴──┘           │▒
    └───────────────────┘▒
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


``:linenos:`` option:

.. code-block:: python
    :linenos:

    print('Hello,')
    print('wooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooorld!')

.. code-block:: python
    :linenos:

    # another code block

``:linenos:`` with ``:lineno-start:``:

.. code-block:: python
    :linenos:
    :lineno-start: 12345

    print('Hello,')
    print('world!')

``:emphasize-lines:``

.. code-block:: python
    :emphasize-lines: 3,5

    def some_function():
        interesting = False
        print('This line is highlighted.')
        print('This one is not...')
        print('...but this one is.')

``:emphasize-lines:`` and ``:linenos:``:

.. code-block:: python
    :linenos:
    :emphasize-lines: 3,5

    def some_function():
        interesting = False
        print('This line is highlighted.')
        print('This one is not...')
        print('...but this one is.')

``:caption:``:

.. code-block:: python
    :caption: This is a ``:caption:``
    :name: code2

    print('Hello, world!')

``:caption:`` and ``:linenos:``:

.. code-block:: python
    :caption: This is another ``:caption:``
    :name: code3
    :linenos:

    print('Hello,')
    print('world!')

See also *[source]* link in :mod:`insipid_sphinx_theme`.


``parsed-literal`` Directive
----------------------------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#parsed-literal

.. parsed-literal::

    Code block with *inline* **markup**, e.g. ``literal text``\ [*]_.

.. [*] Having ``literal text`` within more literal text
    probably doesn't make a lot of sense.

.. parsed-literal::

    Code block with nothing special

.. warning::

   Syntax highlighting (including providing a background color)
   is sometimes broken, see https://github.com/sphinx-doc/sphinx/issues/2167.

Doctest Blocks
--------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#doctest-blocks

>>> print('this is a Doctest block')
this is a Doctest block


Nesting
-------

.. note::

    ::

        'code in note'

    Some text with ``inline code``.

    ::

        'some more code'

.. warning::

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,5

        def some_function():
            interesting = False
            print('This line is highlighted.')
            print('This one is not...')
            print('...but this one is.')

.. topic:: Topic

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,5

        def some_function():
            interesting = False
            print('This line is highlighted.')
            print('This one is not...')
            print('...but this one is.')

..

    ::

        'code in quote'

.. warning::

    definition term
        ::

            'code in definition in admonition'

.. sidebar:: Sidebar

    .. code-block:: python
        :linenos:
        :emphasize-lines: 3,5

        def some_function():
            interesting = False
            print('This line is highlighted.')
            print('This one is not...')
            print('...but this one is.')

.. code-block:: reST

    Code After Sidebar
    ==================

    .

    .

    .

    .

    .

    .

    .

    A long long long long long long long long long long long long long line.
