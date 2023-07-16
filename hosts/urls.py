from django.urls import path

from .views import (hosts_list, create_host, manage_host)

urlpatterns = [
    path('hosts/', hosts_list, name="index"),
    path('hosts/create/', create_host, name="create"),
    path('hosts/<str:pk>/manage/', manage_host, name="manage"),
]

app_name = "hosts"