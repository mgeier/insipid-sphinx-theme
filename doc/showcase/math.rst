Math
====

https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#math

Inline: :math:`a^2 + b^2 = c^2`

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#math

Block:


.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2

Another block:

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-math-domain


Math in Section Title: :math:`e^{i\pi} + 1 = 0`
-----------------------------------------------

With label (since Sphinx 1.8):

.. math:: e^{i\pi} + 1 = 0
   :label: euler

----

Euler's identity, equation :eq:`euler`, was elected one of the
most beautiful mathematical formulas.
