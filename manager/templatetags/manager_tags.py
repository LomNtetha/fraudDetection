from django import template
from django.conf import settings

register = template.Library()


def get_menu_index(path):
    for i, v in enumerate(settings.MENU):
        if v[0] == path:
            return i
    return -1


@register.simple_tag(takes_context=True)
def get_current_menu(context):
    request = context['request']

    path = request.path.split('/')[1]
    menu_index = get_menu_index(path)

    # try:
    previous = settings.MENU[menu_index - 1] if menu_index >0 else None
    # except:
    #     previous = None

    try:
        next = settings.MENU[menu_index + 1]
    except:
        next = None

    return {
        'current': settings.MENU[menu_index],
        'previous': previous,
        'next': next
    }
