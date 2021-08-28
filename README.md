Description
===========

A simple Django FAQ app for demonstration purposes with the following functionnalities:

- Creation and modification of questions
- Creation and modifications of a question's answer
- API endpoints for questions and category resources 

Permissions and accesses are distributed as follow:

- Anyone registered can read any question and its answer
- Anyone registered can ask new questions
- Staff members can answer and modify questions and its answer
- Anyone registered can send a request to the APIs

Requirements
============

 * Python >= 3.8
 * Django == 2.2
 * djangorestframework == 3.12.4

Installation
============
### Configurations to add in `settings.py`

 .. code-block:: python

    INSTALLED_APPS = [
    ...
    'faq',
    'rest_framework',
    ]
    
    TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
    )
    
    LOGIN_REDIRECT_URL = '/faq/category/'
    
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ]
    }
    
### Paths to add in `urls.py`

.. code-block :: python

    from django.conf.urls import include
    from django.contrib import admin
    from django.urls import path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls')),
        path('faq/', include('faq.urls'), name="faq")
    ]

### Migrate the database

 .. code-block:: python

    $ python manage.py migrate

### And voilà

The application comes with preloaded Questions, Answers and Categories.
You can use the following logins to walk around:

- **admin/azerty1234** has staff access 
- **random_guy/azerty1234** has basic access