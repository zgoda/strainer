import datetime

from strainer import child, field, fields, serializer, validators


def test_docs():

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
        release_date=datetime.date(1971, 12, 17)
    )

    assert album_schema.serialize(album) == {
      'artist': {
          'name': 'David Bowie'
        },
      'release_date': '1971-12-17',
      'title': 'Hunky Dory'
    }
    assert album_schema.deserialize(album_schema.serialize(album)) == {
      'artist': {'name': 'David Bowie'},
      'release_date': datetime.date(1971, 12, 17),
      'title': 'Hunky Dory'
    }
    _input = album_schema.serialize(album)
    del _input['artist']
    errors = None
    try:
        album_schema.deserialize(_input)
    except Exception as e:
        errors = e.errors

    assert errors == {'artist': ['This field is required']}
