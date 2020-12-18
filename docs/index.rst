Strainer: Fast Functional Serializers
=====================================

Strainer is a different take on object serialization and validation in python.

It utilizes a functional style over classes.

A Strainer Example

.. code-block:: python

    import datetime
    from strainer import (
        serializer, field, child, formatters, validators, ValidationException
    )

    artist_serializer = serializer(
        field('name', validators=[validators.required()])
    )

    album_schema = serializer(
        field('title', validators=[validators.required()]),
        field(
            'release_date', validators=[validators.required(), validators.datetime()],
            formatters=[formatters.format_datetime()],
        ),
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
        release_date=datetime.datetime(1971, 12, 17)
    )

Given that we can now serialize, deserialize, and validate data

.. code-block:: python

    >>> album_schema.serialize(album)
    {'artist': {'name': 'David Bowie'},
     'release_date': '1971-12-17T00:00:00',
     'title': 'Hunky Dory'}
    >>> album_schema.deserialize(album_schema.serialize(album))
    {'artist': {'name': 'David Bowie'},
     'release_date': datetime.datetime(1971, 12, 17, 0, 0, tzinfo=<iso8601.Utc>),
     'title': 'Hunky Dory'}
    >>> input = album_schema.serialize(album)
    >>> del input['artist']
    >>> album_schema.deserialize(input)
    ValidationException: {'artist': ['This field is required']}

the example has been borrowed from `Marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_


.. toctree::
   :maxdepth: 2

   introduction
   structure
   validators
   formatters
   api


