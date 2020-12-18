from datetime import date, datetime

from strainer import formatters

import pytest


def test_datetime():
    formatter = formatters.format_datetime()
    assert formatter(None) is None
    with pytest.raises(AttributeError):
        formatter('1')
    with pytest.raises(AttributeError):
        formatter(1)

    dt = datetime(1984, 6, 11, 12, 1)
    assert formatter(dt) == '1984-06-11T12:01:00'

    dt = date(1984, 6, 11)
    assert formatter(dt) == '1984-06-11'
