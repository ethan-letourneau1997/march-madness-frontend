from django import template

register = template.Library()


@register.filter
def sort_by_total_points(people):
    return sorted(people, key=lambda x: x.total_points, reverse=True)


@register.filter
def replace_spaces_with_hyphens(value):
    return value.replace(' ', '-')
