# Thari Analysis and management system is the system for Thari Mutual pty (Ltd) 
The system will allow user to take policy online and make claims through online.  The clients are expected to register themselves on the system before they can 
perform any activity online. The system will allow the customer to make claims online and also they will receive their benefits after making claims. However the system will make payment to 
the clients only and only if that client recognized as legitemate. The system will use machine learning to detect fraudulent client and also to help managers and marketing team with descriptive analysis and predictive analysis.

#How to install the project
1. install python and django on your system
2. create a virtual environment  that will help you to run the project
3. clone the project on your local machine e.g desktop/django
5.1 py -m pip install allauth
6.2 py -m pip install django_two_factor
7.3 py -m pip install phonenumbers
8.4 py -m pip install twilio
9.5 py -m pip install stripe
11. configure database to your desired database . please note this system uses MySQL
12. py manage.py makemigrations
13. py manage.py migrate
