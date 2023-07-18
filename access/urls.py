from django.urls import path

from access.views import (index, create_access)
from access.views import (users_list, create_user, manage_user)

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_access, name="create"),

    path("users/", users_list, name="users"),
    path("users/create/", create_user, name="create_user"),
    path("users/<str:pk>/manage/", manage_user, name="manage_users"),
]

app_name = "access"