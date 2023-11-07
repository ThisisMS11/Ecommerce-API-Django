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

## Django ORM
Django ORM (**Object-Relational Mapping**) abstracts away the underlying database-specific queries, so you don't need to write database-specific SQL queries to interact with your chosen database. Instead, you work with Python code and Django's API to define and query your data models. Django ORM takes care of generating the appropriate SQL queries based on the database you're using. This allows you to write database-agnostic code, and you can switch between different database backends (e.g., PostgreSQL, MySQL, SQLite) without having to change your application's code significantly.

