from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'auth'

urlpatterns=[
    path("", TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path("refresh/",TokenRefreshView.as_view(),name='token-refresh')
]