Validators
==========

Validators convert incoming data into the correct format, and also raise excpetions if data is invalid.

Current Validators
------------------

integer
^^^^^^^

Will validate that a value is an integer.

.. code-block:: python

    >>> from strainer import validators
    >>> int_validators = validators.integer()
    >>> int_validators('1')
    1

You can also optionally, clamp an integer to bounds

.. code-block:: python

    >>> from strainer import validators
    >>> int_validators = validators.integer(bounds=(2, 10))
    >>> int_validators('1')
    2

string
^^^^^^^

Will validate that a value is a string

.. code-block:: python

    >>> from strainer import validators
    >>> string_validators = validators.string()
    >>> string_validators(1)
    '1'


You can also apply a ``max_length``. If the string is longer then the ``max_length`` an exception will be thrown.

.. code-block:: python

    >>> from strainer import validators
    >>> string_validators = validators.string(max_length=100)

required
^^^^^^^^

Will validate that a value exists and that it is not falsey. It will accept ``0``, but raise an exception on ``False``, ``None``, ``''``, ``[]``, and ``{}``.

boolean
^^^^^^^

Will coerce value into either a ``True`` or ``False`` value. ``0``, ``False``, ``None``, ``''``, ``[]``, and ``{}`` would all count as ``False`` values, anything else would be ``True``.

datetime/date/time
^^^^^^^^^^^^^^^^^^

These validators will attempt to parse an ISO 8601 string into a python datetime/date/time object.

In case of datetime and time the timezone information is preserved, also the lack of thereof. Timezone aware objects serialize with timezone information, naive objects without it. The same applies to deserialization - if serialized form contains timezone information it will be preserved in deserialized object.

.. versionchanged:: 1.4
    Datetime, date and time now have separate validators.

.. versionchanged:: 1.4
    No default timezone is applied if timezone information is missing during both serialization and deserialization.

Custom Validators
-----------------

A validator returns a function that will be used to validate a value during serialization. You can use the ``export_validator`` function to create a custom validation function.

.. code-block:: python

    from strainer import validators, ValidationException

    @validators.export_validator
    def my_silly_validators(value, context=None):
        if value == 'An apple':
            raise ValidationException("An apple is not silly")
        return '%s is silly.' % (value)

