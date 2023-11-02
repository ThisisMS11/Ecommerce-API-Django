## Connecting MongoDB to Django
```
1. pip install Django djongo dnspython pytz
2. make the changes in the settings.py

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "CLIENT": {
            'host':'mongodb://admin:password@localhost:27017/',
            'port':27017,
            'username':'your_username' (optional),
            'password':'your_password',(optional)
        },
        "NAME":'DjangoMongo1'
    }
}

3.python manage.py migrate

the tables will be built in the MongoDB database.
```
