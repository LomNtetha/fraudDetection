from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . import models
from .models import FraudDetection



#new table 
class  ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=('name','category','price')
admin.site.register(models. Product, ProductAdmin)


class SubscriptionfeatureAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=('name','Product')
	def Product(self,obj):
		return " | ".join([pro.name for pro in obj.product.all()])
admin.site.register(models.subscriptionfeature,SubscriptionfeatureAdmin)


class DiscountAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=('subscriptionPlan','total_months','total_discount')
admin.site.register(models.Discount,DiscountAdmin)


class  ClientAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=('user','full_Names','image_tag','mobile')
admin.site.register(models. Client, ClientAdmin)


class Insurance_subscriptionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=['user','plan','reg_date','price']
admin.site.register(models.Insurance_subscription,Insurance_subscriptionAdmin)


"""Adding of sales and expenses using """

class ExpenseAdmin(ImportExportModelAdmin,admin.ModelAdmin):

	
    list_display = ['slug', 'name','notes']

admin.site.register(models. Expense, ExpenseAdmin)

class ExpenseTransactionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	
	 list_display=['slug','expense','transaction_date','notes','value']	

def get_name(self, obj):
        return obj.expense.name
get_name.admin_order_field  = 'expense'  
admin.site.register(models. ExpenseTransaction, ExpenseTransactionAdmin)


#class SalesTransactionAdmin(admin.ModelAdmin):
	#list_display=['slug','transaction_date','doc_type','notes','value','client']
#def get_name(self, obj):
        #return obj.client.name
#get_name.admin_order_field  = 'client'  
#admin.site.register(models. SalesTransaction, SalesTransactionAdmin)


class SalesLineTransactionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display=['slug','transaction_date','product','quantity','price','value']
def get_name(self, obj):
        return obj.product.name
get_name.admin_order_field  = 'product'  
  
admin.site.register(models. SalesLineTransaction, SalesLineTransactionAdmin)


class FraudDetectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['PolicyNumber', 'RepNumber','Month', 'WeekOfMonth', 'DayOfWeek', 'Make', 'AccidentArea','DayOfWeekClaimed','MonthClaimed','WeekOfMonthClaimed','Sex','MaritalStatus','Age','Fault', 'PolicyType', 'VehicleCategory', 'VehiclePrice', 'Deductible', 'DriverRating', 'Days_Policy_Accident', 'AgeOfVehicle', 'PoliceReportFiled', 'WitnessPresent', 'AgentType', 'NumberOfCars', 'Year', 'FraudFound_P']
admin.site.register(FraudDetection,FraudDetectionAdmin)


#
#admin.site.register( MultiStepFormModel)
    


