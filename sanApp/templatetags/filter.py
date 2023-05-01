from django import template

register = template.Library()


@register.filter
def br(value):
    if value % 3 == 0:
        return True
    return False


@register.filter
def brr(value):
    if value % 2 != 0:
        return True
    return False
