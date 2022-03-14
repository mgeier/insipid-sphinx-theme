Lists
=====

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks

.. note::

    The configuration value :confval:`html_compact_lists`
    influences the display of lists!


Bullet Lists
------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#bullet-lists

A single list item containing a single paragraph:

* A paragraph.

A single list item containing multiple paragraphs:

* A paragraph.

  Another paragraph.

Multiple list items containing a single paragraph each:

* A paragraph.

* Another paragraph.

Multiple list items, some containing multiple paragraphs:

* A paragraph.

* Another paragraph.

  A third paragraph.

Nested lists, each item containing a single paragraph
and/or a single nested list, each item containing ...

* A paragraph.

* Another paragraph.
  
  - A second level paragraph.

  - A second level paragraph with significantly more text in it.
    So much text that there will be at least one line break within the paragraph.
    This will show the difference in spacing between lines and list items.
    Do you see a difference?
    Or is it the same?

* Another first level paragraph.

An example that doesn't fulfill this rule (only the nested sub-list does):

* A paragraph.

* Another paragraph.
  
  - A second level paragraph

  - A second level paragraph

  Yet another paragraph.

Compact lists can be manually forced by using the ``compact`` class:

.. rst-class:: compact

* A paragraph.

* Another paragraph.

  A third paragraph.

Non-compact lists can be manually forced by using the ``open`` class:

.. rst-class:: open

* A paragraph.

* Another paragraph.

Definition term
    * bullet point in definition

    Normal paragraph in definition.

.. admonition:: Admonition

    * bullet point in admonition

.. topic:: Topic

    * bullet point in topic

.. sidebar:: Sidebar

    * bullet point in sidebar

.. topic:: Compact list in topic

    * A paragraph.

    * Another paragraph.

.. topic:: Non-compact list in topic

    * A paragraph.

    * Another paragraph.

      A third paragraph.

* A list item containing admonitions containing further lists:

  .. admonition:: Compact list in admonition

      * A paragraph.

      * Another paragraph.

  .. admonition:: Non-compact list in admonition

      * A paragraph.

      * Another paragraph.

        A third paragraph.


Enumerated Lists
----------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists

1. Item 1 initial text.

   a) Item 1a.
   b) Item 1b.

2. a) Item 2a.
   b) Item 2b.

#. Arabic numerals.

   a) lower alpha)

      (i) (lower roman)

          A. upper alpha.

             I) upper roman)

#. Lists that don't start at 1:

   3. Three

   4. Four

   C. C

   D. D

   iii. iii

   iv. iv

   999. More than four

Nested lists, each item containing a single paragraph
and/or a single nested list, each item containing ...

1. Paragraph.

2. Paragraph.

   a) Second level paragraph

      * Third level paragraph

      * Another third level paragraph

   b) Another second level paragraph

Successive lists:

1. Paragraph.

A. A paragraph in a new list.

.. admonition:: Admonition

    #. enumerated list item in admonition

.. topic:: Topic

    #. enumerated list item in topic

.. sidebar:: Sidebar

    #. enumerated list item in sidebar


``hlist``
---------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-hlist

.. hlist::
    :columns: 3

    * A list of
    * short items
    * that should be
    * displayed
    * horizontally

.. admonition:: Admonition

    .. hlist::
        :columns: 3

        * ``hlist``
        * in
        * admonition

.. topic:: Topic

    .. hlist::
        :columns: 3

        * ``hlist``
        * in
        * topic

.. sidebar:: Sidebar

    .. hlist::
        :columns: 3

        * ``hlist``
        * in
        * sidebar


Definition Lists
----------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists

term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3 : classifier
    Definition 3.

term 4 : classifier one : classifier two
    Definition 4.

term with ``code`` and **bold**
    Definition with ``code`` and **bold**.

.. admonition:: Admonition

    term with ``code`` and **bold**
        in admonition

.. topic:: Topic

    term with ``code`` and **bold**
        in topic

.. sidebar:: Sidebar

    term with ``code`` and **bold**
        in sidebar


Glossary
--------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#glossary

Example link: :term:`source directory` (term will be highlighted).

.. glossary::

    environment
        A structure where information about all documents under the root is
        saved, and used for cross-referencing.  The environment is pickled
        after the parsing stage, so that successive runs only need to read
        and parse new and changed documents.

    source directory
        The directory which, including its subdirectories, contains all
        source files for one Sphinx project.

    term 1
    term 2
        Definition of both terms.

    term with ``code`` and **bold**
        Definition with ``code`` and **bold**.

.. admonition:: Admonition

    .. glossary::
        term in admonition
            definition

        term in admonition with ``code`` and **bold**
            definition

link: :term:`term in admonition`

.. topic:: Topic

    .. glossary::
        term in topic
            definition

        term in topic with ``code`` and **bold**
            definition

link: :term:`term in topic`

.. sidebar:: Sidebar

    .. glossary::
        term in sidebar
            definition

        term in sidebar with ``code`` and **bold**
            definition

link: :term:`term in sidebar`


Field Lists
-----------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-field-lists

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists

:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer

.. admonition:: Admonition

    :field: value

.. topic:: Topic

    :field: value

.. sidebar:: Sidebar

    :field: value


Option Lists
------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists

-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.

.. admonition:: Admonition

    --flag  Description.

.. topic:: Topic

    --flag  Description.

.. sidebar:: Sidebar

    --flag  Description.


Grammars
--------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#grammar-production-displays

Example link: :token:`try_stmt`.

.. productionlist::
    try_stmt: try1_stmt | try2_stmt
    try1_stmt: "try" ":" `suite`
             : ("except" [`expression` ["," `target`]] ":" `suite`)+
             : ["else" ":" `suite`]
             : ["finally" ":" `suite`]
    try2_stmt: "try" ":" `suite`
             : "finally" ":" `suite`
