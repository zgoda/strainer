from .formatters import format_date
from .structure import field
from .validators import datetime, required as required_validator


def date(source_field, target_field=None,
         attr_getter=None, required=False):

    validators = [datetime()]
    if required:
        validators.insert(0, required_validator())

    formatters = [format_date()]

    return field(source_field, target_field=target_field,
                 attr_getter=attr_getter, validators=validators,
                 formatters=formatters)
