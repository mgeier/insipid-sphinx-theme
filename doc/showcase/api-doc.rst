API Documentation
=================

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html


Info Field Lists
----------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists

A link: :func:`send_message`.

.. function:: send_message(sender, recipient, message_body, [priority=1])

   Send a message to a recipient

   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring


Python
------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain

.. py:function:: require(name)

    Hypothetical built-in function.

.. py:module:: my_module
    :platform: Unix
    :synopsis: This is an old module.
    :deprecated:

A link: :func:`hello_world`.

.. py:function:: hello_world([repeat=1])

    Greet the world.

.. py:data:: __name__

    Name of the module.

.. py:exception:: MyException(msg, [severity=7])

    A bad thing happened.

.. py:class:: MyClass

    A useful class.

    .. py:method:: enable(ignore_errors=False)

        Switch it on.

    .. py:staticmethod:: from_file(filename)

        Create class instance from file.

    .. py:classmethod:: whatever(arg)

        Nobody knows what that does.

    .. py:attribute:: data

        Where all the important stuff is stored

    .. py:decoratormethod:: decorate

        Apply festive attire.

.. py:decorator:: decorate

    Make it more cozy.

.. py:function:: compile(source: string, filename, symbol='file') -> ast object

    Do some compilation.


C
--

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-c-domain

.. c:var:: PyObject* PyTypeObject.tp_bases

    Base classes.

.. c:member:: void* ptr

    A pointer.

.. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject* type, Py_ssize_t nitems)

    Allocate stuff.

.. c:macro:: DEBUG

    Show a debugging message.

.. c:type:: MyStruct

    An opaque struct.


C++
---

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cpp-domain

.. cpp:class:: MyBase

    A base class.

.. cpp:class:: MyClass : public MyBase, MyOtherBase

    A derived class.

.. cpp:class:: my_namespace::MyClass

    A class in a namespace.

.. cpp:class:: template<typename T, std::size_t N> std::array

    A class template.

.. cpp:class:: template<typename T> \
               std::array<T, 42>

    Partial specialization.

.. cpp:class:: template<> \
               std::array<bool, 256>

    Full specialization.

.. cpp:function:: bool my_method(int arg1, std::string arg2)

    A function with parameters and types.

.. cpp:function:: bool my_method(int, double)

    A function with unnamed parameters.

.. cpp:function:: const T &std::array::operator[](std::size_t i) const

    An overload for the indexing operator.

.. cpp:function:: operator bool() const

    A casting operator.

.. cpp:function:: constexpr void foo(std::string &bar[2]) noexcept

    A constexpr function.

.. cpp:function:: MyClass::MyClass(const MyClass&) = default

    A copy constructor with default implementation.

.. cpp:function:: template<typename U> \
                  void print(U &&u)

    A function template.

.. cpp:function:: template<> \
                  void print(int i)

    A specialization thereof.

.. cpp:member:: std::string MyClass::my_member

.. cpp:var:: std::string MyClass::my_other_member[N][M]

.. cpp:member:: int a = 42

.. cpp:member:: template<class T> \
                constexpr T pi = T(3.1415926535897932385)

.. cpp:type:: std::vector<int> MyList

    A typedef-like declaration of a type.

.. cpp:type:: MyContainer::const_iterator

    Declaration of a type alias with unspecified type.

.. cpp:type:: MyType = std::unordered_map<int, std::string>

    Declaration of a type alias.

.. cpp:type:: template<typename T> \
              MyContainer = std::vector<T>

    A templated type alias.

.. cpp:enum:: MyEnum

    An unscoped enum.

.. cpp:enum:: MySpecificEnum : long

    An unscoped enum with specified underlying type.

.. cpp:enum-class:: MyScopedEnum

    A scoped enum.

.. cpp:enum-struct:: protected MyScopedVisibilityEnum : std::underlying_type<MySpecificEnum>::type

    A scoped enum with non-default visibility, and with a specified
    underlying type.

.. cpp:enumerator:: MyEnum::myEnumerator

.. cpp:enumerator:: MyEnum::myOtherEnumerator = 42

.. cpp:union:: MyUnion

.. cpp:concept:: template<typename It> std::Iterator

    Proxy to an element of a notional sequence that can be compared,
    indirected, or incremented.

    **Notation**

    .. cpp:var:: It r

       An lvalue.

    **Valid Expressions**

    - :cpp:expr:`*r`, when :cpp:expr:`r` is dereferenceable.
    - :cpp:expr:`++r`, with return type :cpp:expr:`It&`, when
      :cpp:expr:`r` is incrementable.

.. cpp:class:: Data

    .. cpp:union:: @data

        .. cpp:var:: int a

        .. cpp:var:: double b

Explicit ref: :cpp:var:`Data::@data::a`. Short-hand ref: :cpp:var:`Data::a`.

.. cpp:function:: void f(auto &&arg)

    A function template with a single unconstrained template parameter.

.. cpp:function:: void f(std::Iterator it)

    A function template with a single template parameter, constrained by the
    Iterator concept.

.. cpp:function:: std::Iterator{It} void advance(It &it)

    A function template with a template parameter constrained to be an
    Iterator.

.. cpp:class:: std::LessThanComparable{T} MySortedContainer

    A class template with a template parameter constrained to be
    LessThanComparable.

An expression: :cpp:expr:`a * f(a)` (or as text: :cpp:texpr:`a * f(a)`).

A type: :cpp:expr:`const MySortedContainer<int>&`
(or as text :cpp:texpr:`const MySortedContainer<int>&`).


JavaScript
----------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-javascript-domain

.. js:module:: jsmodule

.. js:function:: $.getJSON(href, callback[, errback])

   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.

.. js:class:: MyAnimal(name[, age])

   :param string name: The name of the animal
   :param number age: an optional age for the animal

.. js:data:: jsdata

.. js:attribute:: jsobject.name


reStructuredText
----------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-restructuredtext-domain

.. rst:directive:: foo

    Foo description.

.. rst:directive:: .. bar:: baz

    Bar description.

.. rst:directive:: my-toctree

    Directive.

    .. rst:directive:option:: caption: caption of ToC

        Option.

    .. rst:directive:option:: glob

        Another option.

.. rst:role:: foo

   Foo description.


The Standard Domain
-------------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-standard-domain


Program Options
^^^^^^^^^^^^^^^^

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-option

A link: :option:`rm -r`.

.. program:: rm

.. option:: -r

    Work recursively.


Environment Variables
^^^^^^^^^^^^^^^^^^^^^

https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#directive-envvar

A link: :envvar:`ENV_VAR`.

.. envvar:: ENV_VAR

    Description of environment variable.


Generic Objects
^^^^^^^^^^^^^^^

.. describe:: PAPER

    You can set this variable to select a paper size.

.. object:: SCISSORS

    Destroys the aforementioned object.


``sphinx.ext.autodoc``
-------------------------

A link: :func:`insipid_sphinx_theme.setup`.

.. automodule:: insipid_sphinx_theme
    :members:

****

.. automodule:: example_module
    :members:


``sphinx.ext.autosummary``
--------------------------

.. warning::

    With ``docutils`` versions older than 0.18, the HTML line breaks in the left
    column are not working correctly.  Make sure to use at least
    ``docutils >= 0.18``, which is supported since Sphinx version 5.0.

.. autosummary::

    a_very_useful_function
    TheBestClass

``:nosignatures:``

.. autosummary::
    :nosignatures:

    a_very_useful_function
    TheBestClass
