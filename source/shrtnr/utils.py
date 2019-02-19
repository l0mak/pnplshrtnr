import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 4)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    urlclass = instance.__class__
    qs_exists = urlclass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size+size)
    return new_code