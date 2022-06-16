from django.urls import path

from django.views.generic import TemplateView

from . import views

urlpatterns = [
  path('', views.login, name="login"),
   path('marketing_dashboard.html/', views.marketing_dashboard, name="marketing_dashboard"),
  
   
        
]