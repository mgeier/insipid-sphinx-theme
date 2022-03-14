Some text before the first section title.

Sections
========

Header Level 2
--------------

Header Level 3
^^^^^^^^^^^^^^

Header Level 4
''''''''''''''

Header Level 5
~~~~~~~~~~~~~~

Header Level 6
++++++++++++++

Only levels down to ``<h6>`` are typically supported.

Header Level 2
--------------

Text.

Header Level 3
^^^^^^^^^^^^^^

Text.

Header Level 4
''''''''''''''

Text.

Header Level 5
~~~~~~~~~~~~~~

Text.

Header Level 6
++++++++++++++

Text.


Rubric
------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric

Some text.

.. rubric:: Title of the Rubric

Some text.

.. note::

    Some text.

    .. rubric:: Rubric in admonition

    Some text.

.. topic:: Topic

    Some text.

    .. rubric:: Rubric in topic

    Some text.

.. sidebar:: Sidebar

    Some text.

    .. rubric:: Rubric in sidebar

    Some text.


Table of Contents
-----------------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#table-of-contents

.. contents:: Table of Contents
    :backlinks: none


Local Table of Contents
-----------------------

.. contents::
   :local:

Subsection One
^^^^^^^^^^^^^^

Subsubsection
'''''''''''''

Subsection Two
^^^^^^^^^^^^^^

Nested ``toctree``
------------------

.. toctree::

    nested document
    An External URL <https://www.sphinx-doc.org/>


Another Top-Level Section
=========================

It is uncommon
-- and a bit weird --
to have multiple top-level sections in the same source file.


Subsection
----------

Another nested document:

.. toctree::

    another-nested-document
