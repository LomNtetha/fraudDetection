# Fraud Detection and Analysis System
This is a machine learning and django based system 

This is a web-based fraud detection and sales analysing system for an insurance companies that has three main modules which are Client, Sales support and manager,i developed this system while I was doing my final year at the university. First of all, before I train and test algorithm models to detect fraud, I analyze the datasets following CRISP-DM techniques.


## System Description for Visualization of Data

While working with the dataset, I used  Matplotlib, tabulate and Seaborn to visualize particular information from the dataset. The System has a manager site, where I analyze insurance sales and visualize them in form of graphs such as bar charts and piecharts. The managers are enabled to download the charts in many different forms such as images and Microsoft Excel.  It has sales support site where the sales support are enabled to import and export the data in different formats such as CSV, SQL and Microsoft Excel

## Transparency of Data

The fraud detection part of the system is specifically detecting whether the claim is fraudulent or legitimate while the client claiming for their benefits during an incident. So far the system was enabled to detect whether the claim is fraudulent or legitimate and report or revealed it to the sales support team of the insurance. 

## Main Working Functionality of the System

- Registaring of clients using social apps google
- Two factor authentication using google authenticator and Twillio
- Subscribing for policy and payements with Stripe
- Make claims online 
- fraud Detection
- policy sales analysis and visualing of them inbarcharts and piecharts



## Goals of the System
My goal is to build a fully functioning system that will allow clients to subscribe for policy online.The system suppossed to verify whether the clients are whom they claim they are while registaring and claiming for their benefits using deep learnig algorithms. To buid the system that will predict what will be the sales of policy in comming weeks,months or even years. The system will have recommendations functionality

## Recommendations

My recommendation to everyone in the field of analysing data from large Datasets is to follow CRISP-DM  Techniques while working with large and complicated datasets.

## how to run the System on local Machine

To get started please ensure that python 3.8 or above is installed in your system

- Create a project directory
  ```
  mkdir projectfolder
  ```

- go to project folder
  ```
  cd projectfolder
  ```

- Create virtual environment
  ```
  python -m venv env
  ```
- Activate the virtual environment
  ```
  source env/bin/activate
  ```
- Then clone the project
  ```
  git clone https://github.com/LomNtetha/fraudDetection.git
  ```
- go to project directory
  ```
  cd fraudDetection
  ```

- Install requirements file
  ```
  pip install -r requirements.txt
  ```

- migrate Database
  ```
  python manage.py migrate
  ```

- Create super user
  ```
  python manage.py createsuperuser
  ```

- run the project
  ```
  python manage.py runserver
  ```

## How to push the project on cloud Heroku PAAS

install heroku cli and git on you system and create  account on heroku

- on project directory
  ```
  git add .
  ```

  
- commit changes
 ```
 git commit -m "My comments"
 ```
     
- create project name
  ```
  heroku create
  ```

- Ensure that projet repostory is listed
  ```
  git remote -v
  ```

- push the project to heroku
  ```
  git push heroku master
  ```

- Create migrations and super user
  ```
  heroku run python manage.py migrate
  ```

  ```
  heroku run python manage.py createsuperuser
  ```

- open the project
  ```
  heroku open
  ```

## packages used 
- python 3.10.2 local and python 3.10.6 on heroku
- Django 4.1
- Sqlite local and postgresql heroku
- whitenoise  6.2.0 for static files
- bootstrap 5
- gunicorn 20.1.0 for http and https server request
 

