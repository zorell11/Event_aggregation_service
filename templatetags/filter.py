from django import template
register = template.Library()

@register.filter(name='range')
def range(start, end):
    return list(range(start,end))


register.filter('range', range)
