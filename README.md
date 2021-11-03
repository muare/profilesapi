# profilesapi

## [Udemy Course Link ](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js)
> Course DRF level 3


## Token authentication
### Step 1 - installation

- install django-rest-auth
- install django-allauth

### Step 2 - modification of settings
- api-auth/ from rest_framework.urls are necessary for browsable API
- rest-auth/ from rest_auth.urls are ready for REST API

```
# modification in settings.py

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```
### Step 3 - modification of urls
```
urlpatterns = [
    ...,
    url('rest-auth/', include('rest_auth.urls'))
    url('api-auth/', include('rest_framework.urls'))
]

```

## User registration
### Step 1 - modificatioin of settings
```
INSTALLED_APPS = (
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
)

SITE_ID = 1

```

### Step 2 - modification of urls
```
urlpatterns = [
    ...,
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]
```
