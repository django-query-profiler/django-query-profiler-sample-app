# Coffee Master
**Coffee Master** is a web app that helps cafe run the business. Customers can use the app to place their order while the baristas can receive the orders and prepare the drinks

## Prerequisites
Make sure your machine/env has the below software (tips: use pip to install Django and rest framework)
```
python 3 (i.e. 3.6)
Django 2.0 or above (preferred 2.1.1)
Django REST framework 3.8.2
```

## Getting Started
Execute the below commands in the project rootdir and then open browser to browse to localhost:8000/
```
python3 manage.py migrate
python3 manage.py runserver
```

## Features
* **authentication**: user login and registration system
* **user groups**: two groups of users with different permissions: customer and barista 
* **restricted urls**: Certian urls require users to login and some would require a particular permission 
* **rest api**: use django rest framework to power the api endpoints 
* **auto data loading**: pages are updated without the need to manually refresh the browser 
* **automation test**: automate some tests to ensure that the essential functionalities consistent 
* **clean UI**: super user friendly and easy to use 

## Built with
* **Django** - Backend
* **Vuejs** - Frontend

## APIs
* /food/orderlist/ - GET and POST endpoints to retrieve the order lists and make order
* /food/orderdetail/<order_id> - CRUD endpoints for particular order detail, only admin and baristas users have access

## Test
Execute the below command in the project rootdir to run the test automation
```
python3 manage.py test
```

## Demo
Deploed app@ http://tomliangg.pythonanywhere.com 

demo user1: barista  
pass: demo_abc  

demo user2: customer  
pass: demo_abc  
### Home Page
![Alt text](/img/homepage.png?raw=true "Homepage")

### Order Page
![Alt text](/img/order.png?raw=true "Order")

### Manage Page
![Alt text](/img/manage.png?raw=true "Manage")
