# Purrfect-Match-back-end
<img width="1465" alt="Purrfect_match main" src="https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/de9081e2-159d-42a9-a262-ad671d0597df">

# Front-end deployment:
https://purrfect-match-front-end.vercel.app/

# Back-end deployment:
https://purrfect-match-back-end-7b130ef4f9c3.herokuapp.com

# Overview
PurrfectMatch is built for helping animal adoption. You can view and add the furry friend to adoption list. You will be able to contact the shelter for further application.

# Team
- Backend:
  - Kia: https://github.com/Kdrummmond625
  - Shan: https://github.com/makeyourwon
- Frontend:
  - Joshua: https://github.com/kratos238
  - Kevin: https://github.com/Kevelaz

# Technique
- Django, Python, Node, CORS, JSON, pet-finder API

# User Stories


# ERD
![PurrfectMatch ERD](https://github.com/makeyourwon/Purrfect-Match-back-end/assets/149891853/5d9c7997-c3c7-4239-83d9-f01ef219362d)


# Routing Table                                   
### Backend API URL Paths
#### User Authentication, Registration, and Token Management
| Function              | URL                                  | Method    | Description                    |
|-----------------------|--------------------------------------|-----------|--------------------------------|
| User registration     | /register/            | POST      | User registration.             |
| User login            | /login/               | POST      | User login, returns tokens.    |
| Refresh access token  | /refresh/       | POST      | Refresh access token.          |
#### User Profile Management
| Function               | URL                                   | Method    | Description                   |
|------------------------|---------------------------------------|-----------|-------------------------------|
| Fetch profile details  | /profile/              | GET/PUT      | Fetch user's profile details and update profile info. |
#### Animal Listings and Filters
| Function             | URL                              | Method | Description                        |
|----------------------|----------------------------------|--------|------------------------------------|
| List all animals     | animals/              | GET    | List all animals with filters.     |
| Animal details by ID(primary key) | /animals/pk/     | GET    | Get animal details by ID.              |
#### Favorites Management
| Function                   | URL                                      | Method | Description                      |
|----------------------------|------------------------------------------|--------|----------------------------------|
| List favorited animals     |/favorites/                    | GET    | List single user's favorited animals.   |
| Add an animal to favorites | /favorites/add/pk/                | POST   | Add an animal to one profile's favorites.      |
| Remove an animal from favorites | /favorites/remove/pk/ | POST(DELETE) | Remove an animal from favorites. |

# Setup and Installation
Clone the Repository:
```bash
git clone https://github.com/makeyourwon/Purrfect-Match-back-end.git
```
Start a virtual environment:
```bash
pipenv shell
```
Install dependencies:
```bash
pipenv install django psycopg2-binary djangorestframework
pip install python-dotenv
```
Create your database in sql, in terminal enter:
```bash psql```
Then,
```bash
CREATE DATABASE <Your database name>;

CREATE USER <Username> WITH PASSWORD '<password>';

GRANT ALL PRIVILEGES ON DATABASE <Your database name> TO <Username>;

ALTER DATABASE <Your database name> OWNER TO <Username>;
```
Then enter
```bash
\q
```
to get back to pipenv.
Run:
```bash
python3 manage.py migrate
```
Run below to create superuser for Django api:
```bash
python3 manage.py createsuperuser
```
Seed the database:
```bash
pipenv install djangorestframework-simplejwt django-cors-headers
python3 manage.py import_animals transformed_data_output.json
pipenv install django-filter
```
Setting your settings.py:
```bash
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
  	'rest_framework', # Add this line.
  	'main_app', # Add this line.
]
```
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purrfect_match', # project name.
        # 'HOST': 'localhost',  <-- (optional) some computers might need this line
        # 'USER': 'cat_admin', <-- (optional) postgres user name, if you have to sign into an account to open psql, you will want to add that user name here.
        # 'PASSWORD': 'password', <-- (optional) postgres user password, if you have to sign into an account to open psql, you will want to add that user password here.
        # 'PORT': 3000 <-- if you desire to use a port other than 8000, you can change that here to any valid port id, some number between 1 and 65535 that isn't in use by some other process on your machine. The reason for this port number range is because of how TCP/IP works, a TCP/IP protocol network(the most widely used protocol used on the web) allocated 16 bits for port numbers. This means that number must be greater than 0 and less than 2^15 -1. 
    }
}
```
Set auth:
```bash
# catcollector/settings.py


ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # allows requests from localhost - will need to update again for deployment

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Adjust the port if your frontend runs on a different one
]

# Add 'corsheaders' to INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

# Add 'corsheaders.middleware.CorsMiddleware' to MIDDLEWARE
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

# Configuration for django-rest-framework-simplejwt
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Configuration for simple JWT
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}




# Trello
https://trello.com/b/VbdaIAZh/purrrfect-match

# Timeline

|Date | Todo | Status|
|-----|------|-------|
|2/9  | Create Proposal | Complete|
|2/12 | Complete Scaffolding | Complete |
|2/12 | Get API Key for 3rd party integration | Complete|
|2/12 | Test Routes BackEnd | Complete |
|2/13 | Test Authentication | Complete on 2/12 |
|2/14 | Deployment | Complete |
|2/15 | Style Project | Complete |


# Ice box
1. User reviews
2. List shelters nearby - may require google api
3. volunteering opportunities page for shelters
4. Donations page with link
5. Pet Care Tips for new owners

# Instructors:
Emre, Greg, Grant

# Resources:
https://git.generalassemb.ly/seb-beherenow/django-setup-urls-views






