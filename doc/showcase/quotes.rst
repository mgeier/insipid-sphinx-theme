.. highlight:: none

Quotes
======

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#lists-and-quote-like-blocks


Block Quotes
------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#block-quotes

    A block quote may end with an attribution:
    a text block beginning with ``--``, ``---``, or a true em-dash,
    flush left within the block quote.
    If the attribution consists of multiple lines,
    the left edges of the second and subsequent lines must align.

    -- ``docutils`` documentation

    Multiple block quotes may occur consecutively
    if terminated with attributions::

        Unindented paragraph.

            Block quote 1.

            --Attribution 1

            Block quote 2.

    Empty comments may be used to explicitly terminate preceding constructs
    that would otherwise consume a block quote::

        * List item.

        ..

            Block quote 3.

    Empty comments may also be used to separate block quotes::

            Block quote 4.

        ..

            Block quote 5.

    Blank lines are required before and after a block quote,
    but these blank lines are not included as part of the block quote.

    -- ``docutils`` documentation


.. sidebar:: Block quote in sidebar

    ..

        Block quote.

.. topic:: Block quote in topic

    ..

        Block quote.

.. note::

    ..

        Block quote in an :doc:`admonition <admonitions>`.


Epigraphs
---------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#epigraph

.. epigraph::

    An epigraph is an apposite (suitable, apt, or pertinent) short inscription,
    often a quotation or poem, at the beginning of a document or section.

    -- ``docutils`` documentation


Highlights
----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#highlights

.. highlights::

    * summarize the main points of a document or section
    * often consisting of a list


Pull-Quotes
-----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#pull-quote

.. pull-quote::

    A pull-quote is a small selection of text "pulled out and quoted",
    typically in a larger typeface.
    Pull-quotes are used to attract attention, especially in long articles.

    -- ``docutils`` documentation
