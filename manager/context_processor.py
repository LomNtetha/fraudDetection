from django.conf import settings


def menu(request):
    return {'MENU': settings.MENU}
