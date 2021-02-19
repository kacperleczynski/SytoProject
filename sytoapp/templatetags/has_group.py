from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def has_group(user, group_name='stationary_workers'):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter
def has_group(user, group_name='homeworkers'):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


@register.filter
def has_group(user, group_name='admin'):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False