from django.urls import path

from .views import (index, create_access)

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_access, name="create"),
]

app_name = "access"