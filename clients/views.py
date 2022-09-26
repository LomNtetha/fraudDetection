
import stripe
import json
import logging
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.views.generic import DetailView, FormView
from django_otp.decorators import otp_required

from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.core import serializers
#from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Count
from . import models
import stripe
from . import forms

#imports from machine learning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pandasql import sqldf
from imblearn.over_sampling import SMOTE
import scipy.stats as stats
from tabulate import tabulate
from xgboost import XGBClassifier
from xgboost import plot_tree
from xgboost import plot_importance

# import packages for hyperparameters tuning
#from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
#import hyperopt.pyll
#from hyperopt.pyll import scope
#from hpsklearn import HyperoptEstimator

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

from category_encoders.ordinal import OrdinalEncoder
from category_encoders.binary import BinaryEncoder
from category_encoders.one_hot import OneHotEncoder

from .models import FraudDetection

logger = logging.getLogger(__name__)


User = get_user_model()



def index(request):
   
     return render(request, 'clients/index.html')

# Create your views here.
# Subscription Plans clients from models
def pricing(request):
    pricing=models.Product.objects.annotate(total_members=Count('insurance_subscription__id')).all().order_by('price')
    dfeatures=models.subscriptionfeature.objects.all()
    return render(request, 'clients/index.html',{'plans':pricing,'dfeatures':dfeatures})

# clients details
def clientsDetails(request,plan_id,):
    clientsDetail=models.Product.objects.get(pk=plan_id)
    return render(request, 'clients/clientsDetails.html',{'user':clientsDetail})


# Checkout
def checkout(request,plan_id):
    planDetail=models.Product.objects.get(pk=plan_id)
    return render(request, 'clients/checkout.html',{'plan':planDetail})

stripe.api_key=settings.STRIPE_TEST_SECRET_KEY
def checkout_session(request,plan_id):
    plan=models.Product.objects.get(pk=plan_id)
    session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
          'price_data': {
            'currency': 'LSL',
            'product_data': {
              'name': plan.name,
            },
            'unit_amount': plan.price*100,
          },
          'quantity': 1,
        }],
        mode='payment',

        success_url='https://boiling-earth-35730.herokuapp.com/pay_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://boiling-earth-35730.herokuapp.com/pay_cancel',
        client_reference_id=plan_id
    )
    return redirect(session.url, code=303)

# Success
from django.core.mail import EmailMessage

def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id=session.client_reference_id
    plan=models.Product.objects.get(pk=plan_id)
    user=request.user
    models.Insurance_subscription.objects.create(
        plan=plan,
        user=user,
        price=plan.price,
    )
    #subject='Order Email'
    #html_content=get_template('clients/orderemail.html').render({'title':plan.name})
   # from_email='ntethalumkile@gmail.com'

    #msg = EmailMessage(subject, html_content, from_email, ['lumkilentetha878@gmail.com'])
    #msg.content_subtype = "html"  # Main content is now text/html
    #msg.send()

    return render(request, 'clients/success.html')

# Cancel
def pay_cancel(request):
    return render(request, 'clients/cancel.html')


#views for client dashboard
#@login_required
#@otp_required
def dashboard(request):
      return render(request,'dashboard/fraud.html')

#def predict(request):
#@login_required
#@otp_required
def predict(request):
    return render(request,'dashboard/fraud.html')    
      #return render(request,'dashboard/fraud.html')

#def predict_chances(request):
#@login_required
#@otp_required
def predict_chances(request):
    if request.POST.get('action') == 'post':
        
        Month = int(request.POST.get('Month'))
        WeekOfMonth = int(request.POST.get('WeekOfMonth'))
        DayOfWeek = int(request.POST.get('DayOfWeek'))
        Make = int(request.POST.get('Make'))
        AccidentArea = int(request.POST.get('AccidentArea'))
        DayOfWeekClaimed = int(request.POST.get('DayOfWeekClaimed'))
        MonthClaimed = int(request.POST.get('MonthClaimed'))
        WeekOfMonthClaimed = int(request.POST.get('WeekOfMonthClaimed'))
        Sex = int(request.POST.get('Sex'))
        MaritalStatus = int(request.POST.get('MaritalStatus'))
        Age = int(request.POST.get('Age'))
        Fault = int(request.POST.get('Fault'))
        PolicyType = int(request.POST.get('PolicyType'))
        VehicleCategory = int(request.POST.get('VehicleCategory'))
        VehiclePrice = int(request.POST.get('VehiclePrice'))
        PolicyNumber = int(request.POST.get('PolicyNumber'))
        RepNumber = int(request.POST.get('RepNumber'))
        Deductible = int(request.POST.get('Deductible'))
        DriverRating = int(request.POST.get('DriverRating'))
        Days_Policy_Accident = int(request.POST.get('Days_Policy_Accident'))
        AgeOfVehicle = int(request.POST.get('AgeOfVehicle'))
        PoliceReportFiled = int(request.POST.get('PoliceReportFiled'))
        WitnessPresent = int(request.POST.get('WitnessPresent'))
        AgentType = int(request.POST.get('AgentType'))
        NumberOfCars = int(request.POST.get('NumberOfCars'))
        Year = int(request.POST.get('Year'))

        #unpickle data from jupyter nootebook

        #for herokuapp 
        #clf_dt1 = pd.read_pickle(r"/app/clients/fraud_model.pickle")
        # for local application
        clf_dt1 = pd.read_pickle(r"/home/lumkile/django-projects/insurance/fraudDetection/clients/fraud_model.pickle")
        

        #make predictions
        result = clf_dt1.predict([[Month, WeekOfMonth, DayOfWeek, Make, AccidentArea, DayOfWeekClaimed, MonthClaimed, WeekOfMonthClaimed, Sex, MaritalStatus, Age, Fault, PolicyType, VehicleCategory, VehiclePrice, PolicyNumber, RepNumber, Deductible, DriverRating, Days_Policy_Accident, AgeOfVehicle, PoliceReportFiled, WitnessPresent, AgentType, NumberOfCars, Year]])
        FraudFound_P = result
        FraudDetection.objects.create(Month = Month, WeekOfMonth = WeekOfMonth, DayOfWeek = DayOfWeek, Make = Make, AccidentArea = AccidentArea, DayOfWeekClaimed = DayOfWeekClaimed, MonthClaimed = MonthClaimed, WeekOfMonthClaimed = WeekOfMonthClaimed, Sex = Sex, MaritalStatus = MaritalStatus, Age = Age, Fault = Fault, PolicyType = PolicyType, VehicleCategory = VehicleCategory, VehiclePrice = VehiclePrice, PolicyNumber = PolicyNumber, RepNumber = RepNumber, Deductible = Deductible, DriverRating =DriverRating, Days_Policy_Accident =Days_Policy_Accident, AgeOfVehicle = AgeOfVehicle, PoliceReportFiled = PoliceReportFiled, WitnessPresent = WitnessPresent, AgentType = AgentType, NumberOfCars = NumberOfCars, Year = Year, FraudFound_P = FraudFound_P )
    return render(request,'dashboard/fraud.html') 
   
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": FraudDetection.objects.all()}
    return render(request, "dashboard/results.html", data)

