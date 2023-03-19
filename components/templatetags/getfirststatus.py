import json
import re
from django import template
from django.conf import settings

register = template.Library()


def get_first_status(value, arg):
    if hasattr(value, str(arg)):
        if getattr(value, arg).first():
            return getattr(value, arg)
        return None
    else:
        return None

def setparams(value, arg):
    return value.filter(**json.loads(arg)) if value else None

register.filter('getfirststatus', get_first_status)
register.filter('setparams', setparams)
