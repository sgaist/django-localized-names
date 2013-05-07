"""Template tags for the ``localized_names`` app."""
from django.utils.translation import gettext

from django_libs.format_utils import get_format


def get_name(obj, setting_name='LONG_NAME_FORMAT'):
    """
    Returns the correct order of the name according to the current language.

    """
    nickname = obj.get_nickname()
    romanized_first_name = obj.get_romanized_first_name()
    romanized_last_name = obj.get_romanized_last_name()
    non_romanized_first_name = obj.get_non_romanized_first_name()
    non_romanized_last_name = obj.get_non_romanized_last_name()
    title = gettext(obj.get_title())

    format_string = get_format(setting_name)
    format_kwargs = {}
    if '{n}' in format_string:
        format_kwargs.update({'n': nickname})
    if '{N}' in format_string:
        format_kwargs.update({'N': nickname.upper()})
    if '{f}' in format_string:
        format_kwargs.update({'f': romanized_first_name})
    if '{F}' in format_string:
        format_kwargs.update({'F': romanized_first_name.upper()})
    if '{l}' in format_string:
        format_kwargs.update({'l': romanized_last_name})
    if '{L}' in format_string:
        format_kwargs.update({'L': romanized_last_name.upper()})
    if '{a}' in format_string:
        format_kwargs.update({'a': non_romanized_first_name})
    if '{A}' in format_string:
        format_kwargs.update({'A': non_romanized_first_name.upper()})
    if '{x}' in format_string:
        format_kwargs.update({'x': non_romanized_last_name})
    if '{X}' in format_string:
        format_kwargs.update({'X': non_romanized_last_name.upper()})
    if '{t}' in format_string:
        format_kwargs.update({'t': title})
    if '{T}' in format_string:
        format_kwargs.update({'T': title.upper()})

    return format_string.format(**format_kwargs)
