from django.urls import path
from django.views.generic import TemplateView


from . import views

urlpatterns = [

  

# subscription for clients

	path('',views.pricing,name='pricing'),
	path('',views.index,name='index'),
	path('clientsDetails/<int:plan_id>',views.checkout,name='clientsDetails'),
	path('checkout/<int:plan_id>',views.checkout,name='checkout'),
	path('checkout_session/<int:plan_id>',views.checkout_session,name='checkout_session'),
	path('pay_success',views.pay_success,name='pay_success'),
	path('pay_cancel',views.pay_cancel,name='pay_cancel'),
	# User Dashboard Section Start
  # user dashboard URL 
  path('clients/dashboard/fraud.html', views.dashboard, name="dashboard"),

    path('clients/dashboard', views.predict, name="predict"),

    path('clients/dashboard/', views.predict, name='prediction_page'),
    path('clients/dashboard/fraud/', views.predict_chances, name='submit_prediction'),
    path('clients/dashboard/results/', views.view_results, name='results'),

    ]
