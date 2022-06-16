
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView

from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
#from django.views.static import serve

#from thariauth import settings 


urlpatterns = [

     path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
     path('secret/', admin.site.urls),
     #two factor urls
     path('', include(tf_urls)), 

     #Alluth
     path('accounts/', include('allauth.urls')),
     path('', include('clients.urls')),
     path('agent/', include('agent.urls')),
     path('manager/', include('manager.urls')),
     path('manager/', TemplateView.as_view(template_name="index.html")),
     path('marketing/', include('marketing.urls')),
     #Twilio client URL
     path('', include(tf_twilio_urls)),
     #path('accounts/',TemplateView.as_view(Template_name="account/login")),
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
     #re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

      
      
]
