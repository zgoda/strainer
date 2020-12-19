Strainer-2020: Fast Functional Serializers
==========================================

Strainer-2020 is a different take on object serialization and validation in python.

It utilizes functional style over classes and instead of schema definition it uses pure functions to build serialization mechanisms.

A Strainer Example

.. code-block:: python

    import datetime
    from strainer import (
        serializer, field, child, formatters, validators, ValidationException, fields
    )

    artist_serializer = serializer(
        field('name', validators=[validators.required()])
    )

    album_schema = serializer(
        field('title', validators=[validators.required()]),
        fields.date('release_date', required=True),
        child('artist', serializer=artist_serializer, validators=[validators.required()])
    )

    class Artist():
        def __init__(self, name):
            self.name = name

    class Album():
        def __init__(self, title, release_date, artist):
            self.title = title
            self.release_date = release_date
            self.artist = artist

    bowie = Artist(name='David Bowie')
    album = Album(
        artist=bowie,
        title='Hunky Dory',
        release_date=datetime.date(1971, 12, 17)
    )

Given that we can now serialize, deserialize, and validate data

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

The example has been borrowed from `Marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_


.. toctree::
    :maxdepth: 2

    introduction
    structure
    validators
    formatters
    api
