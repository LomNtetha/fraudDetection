from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import re

from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.template.defaultfilters import date
from django.views.generic import TemplateView
from slick_reporting.views import SlickReportViewBase, SlickReportView as OriginalReportView
from slick_reporting.fields import SlickReportField
from clients.models import SalesLineTransaction, Client, Product
from django.utils.translation import gettext_lazy as _
import inspect
from django.views.generic import TemplateView

User = get_user_model()


class GroupByViewWith2ChartsRaw(OriginalReportView):
    """
    We can have multiple charts, and multiple Calculation fields
    """

    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['name',
               SlickReportField.create(Sum, 'quantity', name='quantity__sum', verbose_name=_('Quantities Sold')),
               SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Value (M)')),
               ]

    chart_settings = [
        {'type': 'pie',
         'engine_name': 'highcharts',
         'data_source': ['quantity__sum'],
         'title_source': ['name'],
         'title': 'Pie Chart (Quantities) Highcharts'
         },
        {'type': 'pie',
         'engine_name': 'chartsjs',
         'data_source': ['quantity__sum'],
         'title_source': ['name'],
         'title': 'Pie Chart (Quantities) ChartsJs'
         },
        {'type': 'bar',
         'engine_name': 'highcharts',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Column Chart (Values)'
         },
        {'type': 'bar',
         'engine_name': 'chartsjs',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Column Chart (Values)'
         },
    ]

class Index(TemplateView):
    template_name = 'manager/simple_report.html'

class SetupView(TemplateView):
    """
    We start by a model that contains the data we want to analyze.

    Consider this example SalesLog model
    """
    template_name = 'manager/simple_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['code'] = inspect.getsource(SalesLineTransaction) + '\n\n' + inspect.getsource(
            Client) + '\n\n' + inspect.getsource(Product)
        context['code_comment'] = self.__class__.__doc__
        context['form'] = None
        return context


class SlickReportView(SlickReportViewBase):
    # template_name = 'slick_example/simple_report.html'
    code = ''
    comment = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['code'] = inspect.getsource(self.__class__)
        # context['code'] = highlight(inspect.getsource(self.__class__), PythonLexer(), HtmlFormatter(style='colorful'))
        code = inspect.getsource(self.__class__)
        # nodoc = re.sub(":\s'''.*?'''", "", code)
        # nodoc = re.sub(':\s""".*?"""', "", nodoc, )
        points = [(x.start(), x.end()) for x in re.finditer('\"\"\"', code)]
        code = code.replace(code[points[0][0]:points[1][1]], '')

        # import pdb; pdb.set_trace()
        context['code'] = self.code or code
        context['code_comment'] = self.comment or self.__doc__

        # context['comment'] = publish_parts(self.comment, writer_name='html')['html_body']
        # context['comment'] = publish_parts(self.__class__.__doc__ or '', writer_name='html')['html_body']

        return context


class SimpleListReport(SlickReportView):
    """
    Let's start by creating a page where we can filter our report_model record / dataset.
    Slick Reporting come with `SlickReportView` CBV.

    By adding this view to your urls.py
        path('', views.SimpleListReport.as_view()),
    You'll see a results page as the shown below
    """
    report_model = SalesLineTransaction
    # the model containing the data we want to analyze

    date_field = 'transaction_date'
    # a date/datetime field on the report model

    # fields on the report model ... surprise !
    columns = ['transaction_date', 'client', 'product', 'quantity', 'price', 'value']


class TimeSeriesWithoutGroupBy(SlickReportView):
    """
    More options:
    ``columns`` support model traversing
    And
    ``format_row`` hook called on each row to do tidy up the results
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    columns = ['transaction_date', 'client__name', 'product__name', 'quantity', 'price', 'value']

    def format_row(self, row_obj):
        """
        A hook to format each row . This method gets called on each row in the results.
        :param row_obj: a dict representing a single row in the results
        :return: A dict representing a single row in the results
        """
        row_obj['transaction_date'] = date(row_obj['transaction_date'], 'd-m-y H:i')

        return row_obj


class GroupByIntro(SlickReportView):
    """
    Let's start aggregating and computing values for groups of data in our report model.

    This an example of "Total Sales Of Each Product"
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'

    group_by = 'product'
    # We can group_by a foreign key or date field

    columns = ['name',
               SlickReportField.create(method=Sum, field='value', name='value__sum', verbose_name=_('Total sold (M)'))
               # a Slick Report Field is responsible for carrying on the needed calculation(s).
               ]


class GroupByView(SlickReportView):
    """
    It's easy to add chart(s) to the view, using `chart_settings` which is a list of object, each object represent a chart
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['name',
               SlickReportField.create(Sum, 'quantity', name='quantity__sum', verbose_name=_('Quantities Sold')),
               ]

    chart_settings = [{
        'type': 'pie',
        'data_source': ['quantity__sum'],  # the name of the field containing the data values
        'title_source': ['name'],  # name of the field containing the data labels
        'title': 'Pie Chart (Quantities) Highcharts',  # to be displayed on the chart
    }]


class GroupByViewWith2Charts(SlickReportView):
    """
    We can have multiple Calculation fields, multiple charts and multiple charting engines !!
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['name',
               SlickReportField.create(Sum, 'quantity', name='quantity__sum', verbose_name=_('Quantities Sold')),
               SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Value M')),
               ]

    chart_settings = [
        {'type': 'pie',
         'engine_name': 'highcharts',  # setting the engine per chart
         'data_source': ['quantity__sum'],
         'title_source': ['name'],
         'title': 'Pie Chart (Quantities) Highcharts'
         },
        {'type': 'pie',
         'engine_name': 'chartsjs',  # setting the engine per chart
         'data_source': ['quantity__sum'],
         'title_source': ['name'],
         'title': 'Pie Chart (Quantities) ChartsJs'
         },
        # Default: fall back to the what's set in SLICK_REPORTING_DEFAULT_CHARTS_ENGINE
        {'type': 'bar',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Column Chart (Values)'
         },
    ]


class TimeSeries(SlickReportView):
    """
    A time series is a series of data points indexed in time order. Most commonly, a time series is a sequence taken at
    successive equally spaced points in time. - from Wikipedia

    In this example we can see how many pieces of each product were sold each month.
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['name']

    time_series_pattern = 'monthly'
    # Possible options are: daily, weekly, semimonthly, monthly, quarterly, semiannually, annually and custom.

    time_series_columns = [
        SlickReportField.create(method=Sum, field='quantity', name='quantity__sum', verbose_name=_('Quantities Sold'))
        # we can have multiple ReportField in the time series columns too !
    ]


class TimeSeriesCustomization(SlickReportView):
    """
    Let's explore more options by SlickReportView.
    ``__time_series__`` special column name
    And
    ``plot_total`` chart setting
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['name',
               '__time_series__',
               # __time_series__ is special column name used to control the placing of the time series columns inside your columns.
               # Default would be appended to the end of the columns.
               SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Grand Sum')),
               ]

    time_series_pattern = 'monthly'
    time_series_columns = [
        SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Sum per month'))
    ]

    chart_settings = [
        {'type': 'bar',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Total quantities per month',
         'plot_total': True  # Plot Totals !
         },
        {'type': 'bar',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Quantities per product per month'
         }
    ]


class NoGroupByTimeSeries(SlickReportView):
    """
    In this example we are telling Slick Reporting to create a monthly time series for the sum of the `value` field.
    However without giving a group_by, so it operate on the all the records
    and gives us a one line sum of all `values` row in the report model.

    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    columns = ['__time_series__',
               SlickReportField.create(Sum, 'value', verbose_name='Grand Total')
               ]

    time_series_pattern = 'monthly'
    time_series_columns = [
        SlickReportField.create(method=Sum, field='value', name='value__sum', verbose_name=_('Sales'))
    ]

    # A chart for our total values
    chart_settings = [
        {'type': 'bar',
         'data_source': ['value__sum'],
         'title_source': ['name'],
         'title': 'Total sales per month',
         'plot_total':True,
         }
    ]


class CrossTabReportView(SlickReportView):
    """
    Crosstab reports, also known as matrix reports, to show the relationships between three or more query items.
    Crosstab reports show data in rows and columns with information summarized at the intersection points.

    *To get a clearer idea on what this report does, please choose Client(s) and check the results.*
    """
    report_model = SalesLineTransaction
    date_field = 'transaction_date'
    group_by = 'product'
    columns = ['slug', 'name']

    # To activate Crosstab
    crosstab_model = 'client'
    # we corsstab on a foreignkey field

    crosstab_columns = [SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Sales'))
                        # To be computed for each chosen entity in the crosstab.
                        ]


class CrosstabCustomization(SlickReportView):
    """
    Let's add some charts and customizations
    ``__crosstab__`` special column name
    and
    ``crosstab_compute_reminder`` controlling if compute reminder is an option or no.
    and
    ``plot_total`` chart setting works on Crosstab too.

    *please choose Client(s) and check the results.*
    """
    report_model = SalesLineTransaction
    report_title = _('Product Client sales Cross-tab')
    date_field = 'transaction_date'

    group_by = 'product'
    columns = ['__crosstab__',  # a special column name to control the placing fot eh crosstab columns inside th results
               'slug', 'name']

    crosstab_model = 'client'
    crosstab_columns = [SlickReportField.create(Sum, 'value', name='value__sum', verbose_name=_('Sales'))]
    crosstab_compute_reminder = True  # if False the "Reminder" Column will not be computed

    chart_settings = [
        {
            'type': 'pie',
            'data_source': ['value__sum'],
            'plot_total': True,  # Plot total works here too
            'title_source': ['name'],
            'title': _('Per Client Total %'),

        },
        {
            'type': 'bar',
            'data_source': ['value__sum'],
            'title_source': ['name'],
            'title': _('Per Client Per Product'),

        },
        {
            'type': 'bar',
            'data_source': ['value__sum'],
            'plot_total': True,
            'title_source': ['name'],
            'stacking': 'normal',
            'title': _('Per Client Total'),

        },

    ]


class LogIns(SlickReportView):
    """
    We can group by date
    In this example, we can count how many user joined each day.
    """

    report_model = User
    date_field = 'date_joined'
    group_by = 'date_joined'
    columns = ['date_joined', 'count__logins']

    chart_settings = [{
        'type': 'bar',
        'data_source': ['count__logins'],
        'title_source': 'date_joined',
        'title': 'Logins Per Day'
    }, ]


class ThankYou(TemplateView):
   template_name = 'manager/thank-you.html'

