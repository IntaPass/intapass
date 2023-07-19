from django.urls import path

from access.views import (index, create_access, manage_access, give_access, remove_access)
from access.views import (users_list, create_user, manage_user)
from access.views import (ssh_keys_list, ssh_key_create, ssh_key_manage)

urlpatterns = [
    path('', index, name="index"),
    path('create/', create_access, name="create"),
    path('manage/<int:pk>/details/', manage_access, name="manage"),
    path('manage/<int:pk>/give-access/', give_access, name="give_access"),
    path('manage/<int:pk>/remove-access/', remove_access, name="remove_access"),

    path("users/", users_list, name="users"),
    path("users/create/", create_user, name="create_user"),
    path("users/<int:pk>/manage/", manage_user, name="manage_users"),

    path("ssh/<int:owner_id>/", ssh_keys_list, name="ssh_keys_list"),
    path("ssh/<int:owner_id>/create/", ssh_key_create, name="ssh_key_create"),
    path("ssh/<int:owner_id>/<int:pk>/manage/", ssh_key_manage, name="ssh_key_manage"),
]

app_name = "access"