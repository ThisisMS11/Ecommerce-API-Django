from django.urls import path
from users.views import UserViews

app_name = "users"

urlpatterns=[
    path('register/',UserViews.as_view(),name='register'),
]