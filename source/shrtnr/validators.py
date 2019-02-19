from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def url_validate(value):
    url_validator = URLValidator()
    validate_value = value
    if 'http' in validate_value:
        new_value = validate_value
    else:
        new_value = 'http://' + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError('Invalid URL')
    return new_value
