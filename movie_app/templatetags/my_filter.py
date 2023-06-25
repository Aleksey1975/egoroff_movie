from django import template

register = template.Library()


@register.filter(name='my_round')
def my_round(value, x=0):
    return str(round(value, x))[:-2]
