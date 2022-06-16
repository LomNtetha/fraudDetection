from django.db.models import Count
from slick_reporting.fields import SlickReportField
from slick_reporting.registry import field_registry
from django.utils.translation import gettext_lazy as _

field_registry.register(
    SlickReportField.create(method=Count, field='id', name='count__logins', verbose_name=_('Count')))
