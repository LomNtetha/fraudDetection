from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
   
     return render(request, 'marketing/index.html')

def calendar(request):
      return render(request,'marketing/calendar.html' )

def charts(request):
      return render(request,'marketing/charts.html')
      
def contact(request):
      return render(request,'marketing/contact.html')

def login(request):
    return render(request,'marketing/login.html')


def marketing_dashboard(request):
      return render(request,'marketing/marketing_dashboard.html')

def email(request):
      return render(request,'marketing/email.html')

def generalElements(request):
      return render(request,'marketing/general_elements.html') 

def icons(request):
      return render(request,'marketing/icons.html')     

def invoice(request):
      return render(request,'marketing/invoice.html')   

def map(request):
      return render(request,'marketing/map.html')  

def mediaGallery(request):
      return render(request,'marketing/media_gallery.html')  

def price(request):
      return render(request,'marketing/price.html')

def profile(request):
      return render(request,'marketing/profile.html')      

def project(request):
      return render(request,'marketing/project.html')     

def settings(request):
      return render(request,'marketing/settings.html')  

def tables(request):
      return render(request,'marketing/tables.html')    

def widgets(request):
      return render(request,'marketing/widgets.html')      