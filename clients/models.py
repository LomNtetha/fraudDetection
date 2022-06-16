from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.utils.translation import gettext_lazy as _

from django_cryptography.fields import encrypt

import json



# New Subscription Plans Tables
class Product(models.Model):
    CATEGORY = (
        ('Life Cover', 'Life Cover'),
        ('Motor', 'Motor'),
        ('House', 'House'),
        ('Business', 'Business'),
    )
    
    #class duration(models.IntegerChoices):
     #   Month = 1
      #  Three_Months = 3
       # six_Months = 6
        #year = 12
    
    slug = models.SlugField(_('Policy Number'), max_length=50, unique=True, db_index=True, blank=True)
    name = models.CharField(_('Name'), max_length=255, unique=True, db_index=True)
    category = encrypt(models.CharField(max_length=200, null=True, choices=CATEGORY))
    price=models.IntegerField()
    #members_number=models.IntegerField(null=True)
    #duration = models.IntegerField(choices=duration.choices)
 
    class Meta:
        verbose_name = _('subscription plan')
        verbose_name_plural = _('subscription plans')

    def __str__(self):
        return self.name

# Subscription Plans Features
class subscriptionfeature(models.Model):
    
    #subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
   product=models.ManyToManyField(Product)
   name=encrypt(models.CharField(max_length=150))
   
   class Meta:
        verbose_name = _('subscription feature')
        verbose_name_plural = _('subscription features')
        
def __str__(self):
        return self.name


# Package Discounts
class Discount(models.Model):
    subscriptionPlan=models.ForeignKey( Product, on_delete=models.CASCADE,null=True)
    total_months=models.IntegerField()
    total_discount=models.IntegerField()

    def __str__(self):
        return str(self.total_months)

# Subscriber /Clients
class Client(models.Model):
    
    
    slug = models.SlugField(_('Code'), max_length=50, unique=False, db_index=True, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_Names = encrypt(models.CharField(max_length=200, null=True))
    mobile=encrypt(models.CharField(max_length=20))
    address=encrypt(models.TextField())
    img=encrypt(models.ImageField(upload_to="subs/",null=True))


    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __str__(self):
        return str(self.user)

    def image_tag(self):
        if self.img:
            return mark_safe('<img src="%s" width="80" />' % (self.img.url))
        else:
            return 'no-image'

@receiver(post_save,sender=User)
def create_client(sender,instance,created,**kwrags):
    if created:
        Client.objects.create(user=instance)

# Subscription
class Insurance_subscription(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    plan=models.ForeignKey( Product, on_delete=models.CASCADE,null=True)
    price=encrypt(models.FloatField(max_length=50))
    reg_date=encrypt(models.DateField(auto_now_add=True,null=True))

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')

def __str__(self):
        return str(self.clients)

class Expense(models.Model):
    slug = models.SlugField(_('Expense No:'), help_text=_('For fast recall'), max_length=50,
                            unique=True, db_index=True, blank=True)
    name = models.CharField(_('Name'), max_length=255, unique=True, db_index=True)
    notes = encrypt(models.TextField(_('Notes'), null=True, blank=True))

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')

    def __str__(self):
        return self.name


class ExpenseTransaction(models.Model):
    
    slug = models.SlugField(_('Exp Invoice No:'), max_length=50, db_index=True, validators=[], blank=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(_('date'), db_index=True)
    #doc_type = models.CharField(max_length=30, db_index=True)
    notes = models.TextField(_('notes'), null=True, blank=True)
    value = models.DecimalField(_('Amount'), max_digits=19, decimal_places=2, default=0)

    

    class Meta:
        verbose_name = _('Expense Transaction')
        verbose_name_plural = _('Expense Transactions')


#class SalesTransaction(models.Model):
    
  #  slug = models.SlugField(_('refer code'), max_length=50, db_index=True, validators=[], blank=True)
  #  transaction_date = models.DateTimeField(_('date'), db_index=True)
   # doc_type = models.CharField(max_length=30, db_index=True)
   # notes = models.TextField(_('notes'), null=True, blank=True)
    #value = models.DecimalField(_('value'), max_digits=19, decimal_places=2, default=0)

   # client = models.ForeignKey(Client, on_delete=models.CASCADE)

   # class Meta:
      #  verbose_name = _('Sale')
      #  verbose_name_plural = _('Sales')


class SalesLineTransaction(models.Model):
    """
    Sales Log
    """

    slug = models.SlugField(_('Policy Number'), max_length=50, db_index=True, validators=[], blank=True)
    transaction_date = models.DateTimeField(_('Date'), db_index=True)
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(_('Quantity'), max_digits=19, decimal_places=2, default=0)
    price = models.DecimalField(_('Price'), max_digits=19, decimal_places=2, default=0)
    value = models.DecimalField(_('Total Amount'), max_digits=19, decimal_places=2, default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.value = self.price * self.quantity
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = _('Sale Transaction')
        verbose_name_plural = _('Sales Transactions')
#Building fraud detection models
class FraudDetection(models.Model):
     class Month(models.IntegerChoices):
        Jan = 1
        Feb = 2
        Mar = 3
        Apr = 4
        May = 5
        Jun = 6
        Jul = 7
        Aug = 8
        Sep = 9
        Oct = 10
        Nov = 11
        Dec = 12

     Month = models.IntegerField(choices=Month.choices) 
     WeekOfMonth = models.IntegerField()

     class DayOfWeek(models.IntegerChoices):
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6
        Sunday = 7
     DayOfWeek = models.IntegerField(choices=DayOfWeek .choices) 

     class Make(models.IntegerChoices):
        Honda = 1
        Toyota = 2
        BMW = 3
        VW = 4
        Mazda = 5
        Mecedes = 6
        Nisson = 7
        Ford = 8
        Chevrolet = 9
        Jaguar = 10
        Lexus = 11
        Other = 12
     Make = models.IntegerField(choices=Make .choices) 

     class AccidentArea (models.IntegerChoices):
        Urban = 1
        Rural = 0
     AccidentArea = models.IntegerField(choices=AccidentArea .choices) 

     
     class DayOfWeekClaimed (models.IntegerChoices):
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6
        Sunday = 7
     DayOfWeekClaimed  = models.IntegerField(choices=DayOfWeekClaimed.choices) 

     class MonthClaimed (models.IntegerChoices):
        Jan = 1
        Feb = 2
        Mar = 3
        Apr = 4
        May = 5
        Jun = 6
        Jul = 7
        Aug = 8
        Sep = 9
        Oct = 10
        Nov = 11
        Dec = 12

     
     MonthClaimed  = models.IntegerField(choices= MonthClaimed .choices) 
     
     WeekOfMonthClaimed = models.IntegerField()

     class Sex(models.IntegerChoices):
        Female = 1
        Male = 0
     Sex = models.IntegerField(choices=Sex .choices) 

     class MaritalStatus(models.IntegerChoices):
        Married = 1
        Single = 2
        Widow = 3
        Divorced = 4
     MaritalStatus = models.IntegerField(choices=MaritalStatus .choices)

     Age = models.IntegerField() 

     class Fault(models.IntegerChoices):
        Policy_Holder = 1
        Third_Party = 0
     Fault = models.IntegerField(choices=Fault.choices) 

     class PolicyType (models.IntegerChoices):
        Sedan_All_Perils = 1
        Sedan_Collision = 2
        Sedan_Liability = 3
        Sport_All_Perils = 4
        Sport_Collision = 5
        Sport_Liability = 6
        Utility_All_Perils = 7
        Utility_Collision = 8
        Utility_Liability = 9
        Other = 10
     PolicyType = models.IntegerField(choices= PolicyType.choices) 

     
     class VehicleCategory(models.IntegerChoices):
        Sedan = 1
        Sport = 2
        Utility = 3
        Other = 4
     
     VehicleCategory = models.IntegerField(choices=VehicleCategory .choices)

     class VehiclePrice(models.IntegerChoices):
        
        Less_than_20000 = 19999
        Around_20000 = 24500
        Around_30000 = 34500
        More_than_69000 = 69001
        Between_40000_To_59000 = 49500
        Around_60000 = 64500
       
     VehiclePrice = models.  IntegerField(choices=VehiclePrice.choices)
     
     PolicyNumber = models.IntegerField()
     
     RepNumber = models.IntegerField()
     
     Deductible = models.FloatField()

     DriverRating = models.IntegerField()

     class Days_Policy_Accident(models.IntegerChoices):
        Less_than_7 = 4
        More_than_8 = 11
        More_than_15 = 22
        More_than_30 = 31
     Days_Policy_Accident = models.  IntegerField(choices=Days_Policy_Accident .choices)

     
     class AgeOfVehicle(models.IntegerChoices):
        New = 0
        Two_Years= 2
        Three_Years = 3
        Four_Years= 4
        Five_years = 5
        Six_Years= 6
        Seven_Years = 7
        More_Than_Seven_Years = 8
     AgeOfVehicle = models.IntegerField(choices=AgeOfVehicle.choices) 

     
     class PoliceReportFiled (models.IntegerChoices):
        Yes = 1
        No = 0
     PoliceReportFiled = models.IntegerField(choices=PoliceReportFiled.choices) 

     
     class WitnessPresent(models.IntegerChoices):
        Yes = 1
        No = 0
     WitnessPresent = models.IntegerField(choices=WitnessPresent.choices) 

     
     class AgentType(models.IntegerChoices):
        Internal = 0
        External = 1
     AgentType = models.IntegerField(choices=AgentType.choices) 

     
     class NumberOfCars(models.IntegerChoices):
        One_Vehicle = 1
        Two_Vehicle = 2
        Three_To_Four = 4
        Five_To_Eight = 7
        More_than_Eight = 9
     NumberOfCars = models.IntegerField(choices=NumberOfCars.choices)

     Year = models.IntegerField()

     class FraudFound_P(models.IntegerChoices):
        Fraudulent = 0
        Legitemate = 1
     FraudFound_P = models.IntegerField(choices=FraudFound_P.choices) 
     #FraudFound_P = models.IntegerField()

     class Meta:
        verbose_name = _('Claim Policy')
        verbose_name_plural = _('Claim Policies')

     def __str__(self):
        return str(self.PolicyNumber)



"""class MultiStepFormModel(models.Model):
    id=models.AutoField(primary_key=True)
    
    fname=encrypt(models.CharField(max_length=255))
    lname=encrypt(models.CharField(max_length=255))
    phone=encrypt(models.CharField(max_length=255))
    twitter=encrypt(models.CharField(max_length=255))
    facebook=encrypt(models.CharField(max_length=255))
    gplus=encrypt(models.CharField(max_length=255))
    email=encrypt(models.CharField(max_length=255))
    password=encrypt(models.CharField(max_length=255))
    objects=models.Manager()"""
    
     
     