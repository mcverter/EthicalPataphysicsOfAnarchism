from django import template

register = template.Library()


@register.filter()
def filter_by_letter(value_dict: dict, letter: str):
    if not letter:
        return value_dict
    return [v for v in value_dict if v.startswith(letter)]
