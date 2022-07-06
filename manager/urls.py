from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from manager import views
urlpatterns = [
                
                  path('', views.GroupByViewWith2Charts.as_view(), name='group-by-with-several-charts'),
                  path('group-by-date', views.LogIns.as_view(), name='group-by-date'),
                 path('raw/', views.GroupByViewWith2ChartsRaw.as_view()),
                  path('setup/', views.SetupView.as_view(), name='report-model'),
                  path('no-group-by/', views.SimpleListReport.as_view(), name='simple-filer'),
                  path('no-group-by-plus-charts/', views.TimeSeriesWithoutGroupBy.as_view(), name='no-group-by-plus-charts'),
                  path('time-series-without-group-by/', views.NoGroupByTimeSeries.as_view(), name='time-series-without-group-by'),

                  path('group-by/', views.GroupByIntro.as_view(), name='group-by'),
                  path('group-by-chart/', views.GroupByView.as_view(), name='group-by-chart'),
                 # path('group-by-date/', views.LogIns.as_view(), name='group-by-date'),

                  path('time-series/', views.TimeSeries.as_view(), name='time-series'),
                  path('time-series-charts/', views.TimeSeriesCustomization.as_view(), name='time-series-charts'),
                 # path('crosstab/', views.CrossTabReportView.as_view()),
                 # path('crosstab-charts/', views.CrosstabCustomization.as_view()),

                 # path('thank-you', views.ThankYou.as_view()),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


