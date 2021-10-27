Tables
======

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tables


Grid Tables
-----------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+


Simple Tables
-------------

https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables

=====  =====  =======
  A      B    A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

With column spans:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

With more complicated stuff:

=====  =====
col 1  col 2
=====  =====
1      Second column of row 1.
2      Second column of row 2.
       Second line of paragraph.
3      - Second column of row 3.

       - Second item in bullet
         list (row 3, column 2).
\      Row 4; column 1 will be empty.
5      Second column of row 5.

       - Bullet

       Text after bullet.
6      Numbered list:

       #. item
=====  =====

Adjacent tables (is there a vertical space between them?):

+-------+-------+
| col 1 | col 2 |
+-------+-------+

=====  =====
col 1  col 2
=====  =====

CSV Tables
----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table

.. csv-table:: Frozen ``Delights``!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"


List Tables
-----------

https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table

.. list-table:: Frozen ``Delights``!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!


Large Table
-----------

.. csv-table:: A wide table
    :header: Label,Parameter1,Parameter2,Parameter3,Parameter4,Measure1,Measure2,Measure3

    Some fancy name1,first linear classifier,flying,denoised,emotional,0.9,0.6,3.12
    Some fancy name2,second linear classifier,driving,noisy,emotional,0.8,0.6,4.23
    Some fancy name3,third linear classifier,circling,denoised,non emotional,0.7,0.6,8.46
    Some fancy name4,fourth linear classifier,moving,noisy,non emotional,0.6,0.6,8.23
    Some fancy name5,fifth linear classifier,dancing,denoised,emotional,0.4,0.6,9.37
    Some fancy name6,sixth linear classifier,sliding,noisy,emotional,0.8,0.6,4.32
    Some fancy name7,seventh linear classifier,walking,denoised,non emotional,0.9,0.6,2.12
    Some fancy name8,eighth linear classifier,diving,noisy,emotional,0.2,0.4,4.32
    Some fancy name9,ninth linear classifier,strolling,denoised,non emotional,0.5,0.6,2.42



Nesting
-------

.. admonition:: Table in admonition

    +----------------------+
    | Header with ``code`` |
    +======================+
    |  Text with ``code``  |
    +----------------------+

.. topic:: Table in topic

    +----------------------+
    | Header with ``code`` |
    +======================+
    |  Text with ``code``  |
    +----------------------+

.. sidebar:: Table in sidebar

    +----------------------+
    | Header with ``code`` |
    +======================+
    |  Text with ``code``  |
    +----------------------+
