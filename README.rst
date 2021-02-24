Strainer-2020: Fast Functional Serializers
==========================================

Strainer-2020 is a different take on serialization and validation in python. It utilizes a functional style over classes.

Strainer-2020 officially supports Python 3.6 and newer, and runs great on PyPy.

This is a fork of original Alex Kessinger `pystrainer <https://github.com/voidfiles/strainer>`_ library with improvements that changed operation but not the usage paradigm. I'm trying to keep his commitment to efficiency.

Features
--------

- Functional
- Complex Python object serialization
- Data deserialization into simple Python structures
- Data validation

Changes
-------

- serialization is done by data serializers defined for fields
- validators perform data validation only
- basic field types have simplified interface functions tthat wrap generic ``field()`` function
- datetime/time serialization and deserialization preserves timezone information or lack of it; naive datetimes/times are serialized as naive and then deserialized as naive too

Serialization Example
---------------------

.. code-block:: python

    import datetime
    from strainer import (serializer, field, child,
                          formatters, validators,
                          ValidationException, fields)

    artist_serializer = serializer(
        field('name', validators=[validators.required()])
    )

    album_schema = serializer(
        field('title', validators=[validators.required()]),
        fields.date('release_date', required=True),
        child('artist', serializer=artist_serializer, validators=[validators.required()])
    )

    class Artist(object):
        def __init__(self, name):
            self.name = name

    class Album(object):
        def __init__(self, title, release_date, artist):
            self.title = title
            self.release_date = release_date
            self.artist = artist

    bowie = Artist(name='David Bowie')
    album = Album(
        artist=bowie,
        title='Hunky Dory',
        release_date=datetime.datetime(1971, 12, 17)
    )

Now we can serialize, deserialize, and validate data

.. code-block:: python

    >>> album_schema.serialize(album)
    {'artist': {'name': 'David Bowie'},
     'release_date': '1971-12-17',
     'title': 'Hunky Dory'}
    >>> album_schema.deserialize(album_schema.serialize(album))
    {'artist': {'name': 'David Bowie'},
     'release_date': datetime.date(1971, 12, 17),
     'title': 'Hunky Dory'}
    >>> input = album_schema.serialize(album)
    >>> del input['artist']
    >>> album_schema.deserialize(input)
    ValidationException: {'artist': ['This field is required']}

The example has been borrowed from `Marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_ and tweaked.

Installation
------------

To install Strainer-2020, simply:

.. code-block:: bash

    $ pip install strainer-2020
    ✨🍰✨

Satisfaction, guaranteed.
