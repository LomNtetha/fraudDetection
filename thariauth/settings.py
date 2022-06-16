
import os
from pathlib import Path
from typing import Optional

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r*#e_37iw!v-&41#-#42_7jp))m^p%r_p30^jvsfw421t5$_(n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#''
"""
All apps that are used by the system installed here 

"""

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'clients.apps.ClientsConfig',
    'agent.apps.AgentConfig',
    'manager.apps.ManagerConfig',
    'marketing.apps.MarketingConfig',
    
  #'accounts.apps.AccountsConfig',
 
 #'campaigns.apps.CampaignsConfig',
 #'core.apps.CoreConfig',
 #'lists.apps.ListsConfig',
 #'notifications.apps.NotificationsConfig',
 #'subscribers.apps.SubscribersConfig',
 #'templates.apps.TemplatesConfig',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

   'allauth',
   'allauth.account',
   'allauth.socialaccount',
   'allauth.socialaccount.providers.google',
   'crispy_forms',
   #twofactor'
   'django_otp',
   'django_otp.plugins.otp_static',
   'django_otp.plugins.otp_totp',
   'two_factor',
   
  'mathfilters',
  'analytical',
  'request',
  'slick_reporting',
  'channels',
 #'channels_redi
  'admin_honeypot',
 #'django-cryptography',
 

]    


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Always include for two-factor auth
    'django_otp.middleware.OTPMiddleware',
    # Include for Twilio gateway
    'two_factor.middleware.threadlocals.ThreadLocals',
    #add request analytics
    'request.middleware.RequestMiddleware',
    #Add ploptly dash middleware
   #'django_plotly_dash.middleware.BaseMiddleware'  
]

ROOT_URLCONF = 'thariauth.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
               'manager.context_processor.menu'
            ],
             'libraries':{
            'check_package': 'clients.templatetags.check_package',
            'manager_tags': 'manager.templatetags.manager_tags',
            
            }
        },
    },
]

WSGI_APPLICATION = 'thariauth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    

    # `allauth` specific authentication methods, such  as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-file

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
STATIC_ROOT ='var/www/thari/assets/'


#STATICFILES_DIRS = [
 #   BASE_DIR / "static",
  #  '/var/www/static/',
#]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
#CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
"""
Settings for social accounts Authentication such as facebook and  Google


"""

SITE_ID = 1
#Authenticate face book to application
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v7.0',
    }   
}
# Sending emails using SMTP host server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = "ntethalumkile@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "50899604"

ACCOUNT_EMAIL_VERIFICATION ="mandatory"

ACCOUNT_CONFIRM_EMAIL_ON_GET=True

#redirecting Unregister clients back to login if they try to login
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL='two_factor:login'

LOGIN_REDIRECT_URL = 'dashboard'
#login either by email or username
ACCOUNT_AUTHENTICATION_METHOD =  "username_email"
#forcing cutomer to login using email
ACCOUNT_EMAIL_REQUIRED = True
#settings the username to be Uppercases
ACCOUNT_PRESERVE_USERNAME_CASING = False
#Automatically login after email confirmation
#ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL=True

SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
#adding extra sign in fields
#ACCOUNT_FORMS = {
#'signup': 'clients.forms.CustomSignupForm',
#}
"""
Setttiings for two factor Authentication

"""
LOGIN_URL = 'two_factor:login'

LOGOUT_REDIRECT_URL='two_factor:login'

TWO_FACTOR_PATCH_ADMIN=False

TWO_FACTOR_SMS_GATEWAY= 'two_factor.gateways.twilio.gateway.Twilio'

TWO_FACTOR_CALL_GATEWAY= 'two_factor.gateways.twilio.gateway.Twilio'

#TWO_FACTOR_REMEMBER_COOKIE_AGE='activate'

#TWO_FACTOR_CALL_GATEWAY = 'two_factor.gateways.fake.fake'
#TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'

#LOGOUT_REDIRECT_URL= 'account_login'

TWILIO_ACCOUNT_SID= 'AC6398d7e0b8c676f0d9b307f1ccca8e63'
TWILIO_AUTH_TOKEN= 'b78179ec2b17e9edbae2db06d1c421d8'
TWILIO_CALLER_ID='+19402363186'
#TWILIO_MESSAGING_SERVICE_SID='MGd15d161e21b2f6ab640e2249a9044074'


#AUTH_USER_MODEL = 'clients.CustomUser'
"""

Settings for Stripe payment
"""

STRIPE_TEST_PUBLIC_KEY = 'pk_test_51Ke3hVHJdOtHtnwsMnWowUfvjwvwQlaiZjGe5MQQVhK6elRlClCLphJWrxN6O3PkWMN08mvnbQjpPVgkizExJv7L00Z9YxWoft'
STRIPE_TEST_SECRET_KEY = 'sk_test_51Ke3hVHJdOtHtnwsenSvBtruTbOv3Hb5Se3Eh9OGbA8eKE7OW1mJNcpEIDdIvp57kaWWl7yvkwUbRI0C1CcMCcmF00jIh6vfAg'
STRIPE_LIVE_MODE = False

"""
Settings for customizing admin dashboard using 
Jazziming admin dashboard Templates
"""

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Sales Support",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "ThariMutual",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Sales Support",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "clients/images/logo/newlogo.jpg",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the ThariMutual",

    # Copyright on the footer
    "copyright": "ThariMutual (Pty) Ltd",
    
     
    "show_ui_builder":True,



     # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://api.whatsapp.com/send?phone=26650899604", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        
    ],

 
}
JAZZMIN_SETTINGS["show_ui_builder"] = True

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-warning",
    "navbar": "navbar-white navbar-warning",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "Accent_Color_Variants": "warning",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark",
    #"navbar": "text-white",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}

"""Django analytics for tracking and analysis"""

CLICKY_SITE_ID='101362724',
 
"""Slick analyers"""

from django.utils.translation import gettext_lazy as _

MENU = (
    #('', _('Welcome')),
    #('setup', _('Report Model')),
    #('no-group-by', _('Simple Filter')),

    #('no-group-by-plus-charts', _('Simple Filter tidying up')),


    ('group-by', _('Total Sales per Policy')),
    ('group-by-chart', _('Total Number of Policy')),
    ('group-by-with-several-charts', _('Different Charts For Policy')),
    ('group-by-date', _('Login Analysis')),

    ('time-series', _('Number of Policy Sold')),
    ('time-series-charts', _('Analysis of Policy Per Month')),
    ('time-series-without-group-by', _('Total Sales Per Month')),

    #('crosstab', _('Crosstab')),
    #('crosstab-charts', _('Crosstab Customization')),

    # ('crosstab-charts', _('Integration in your own views')),
    # ('crosstab-charts', _('Writing your own chart')),

    # ('crosstab-charts', _('Form Customization')),
    # ('crosstab-charts', _('ReportFields')),
    ('thank-you', _('Reports')),

)


ASGI_APPLICATION = 'thariauth.routing.application'
#CHANNEL_LAYERS = {
 #   'default': {
  #      'BACKEND': 'channels_redis.core.RedisChannelLayer',
   #     'CONFIG': {
    #        'hosts': [('127.0.0.1', 6379),],
     #   }
   # }
#}
# Settings for Encryption and Decryption of The data
#CRYPTOGRAPHY_BACKEND = 'cryptography.hazmat.backends.default_backend()',
#CRYPTOGRAPHY_DIGEST = 'cryptography.hazmat.primitives.hashes.SHA256',
#CRYPTOGRAPHY_KEY = 'CRYPTOGRAPHY_KEY',
#CRYPTOGRAPHY_SALT = 'django-cryptography',