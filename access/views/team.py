from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.models import Group

from access.forms import UserForm

# def groups_list(request):
#     pass

# def create_group(request):
#     pass

# def update_group(request, pk=None):
#     pass

@login_required
def users_list(request):
    users = User.objects.all().order_by("-pk")
    context = {
        "users": users
    }
    return render(request, "team/users/index.html", context=context)

@login_required
def create_user(request):
    form = UserForm((request.POST or None))
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(resolve_url("access:users"))
    context = {
        "form": form
    }
    return render(request, "team/users/create.html", context=context)

@login_required
def manage_user(request, pk=None):
    user = User.objects.get(pk=pk)
    form = UserForm((request.POST or None), instance=user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(resolve_url("access:users"))
    context = {
        "form": form,
        "record": user
    }
    return render(request, "team/users/manage.html", context=context)