from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required

from access.forms import SSHKeysForm
from access.models import SSHKeys

@login_required
def ssh_keys_list(request, owner_id=None):
    ssh_keys = SSHKeys.objects.filter(owner_id=owner_id).order_by("-pk")
    context = {
        "ssh_keys": ssh_keys,
        "owner_id": owner_id
    }
    return render(request, "team/ssh_keys/index.html", context=context)

@login_required
def ssh_key_create(request, owner_id=None):
    form = SSHKeysForm((request.POST or None))
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner_id = owner_id
            instance.save()
            return redirect(resolve_url("access:ssh_keys_list", owner_id=owner_id))
    context = {
        "form": form,
        "owner_id": owner_id
    }
    return render(request, "team/ssh_keys/create.html", context=context)

@login_required
def ssh_key_manage(request, pk=None, owner_id=None):
    ssh_key = SSHKeys.objects.get(pk=pk, owner_id=owner_id)
    form = SSHKeysForm((request.POST or None), instance=ssh_key)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner_id = owner_id
            instance.save()
            return redirect(resolve_url("access:ssh_keys_list", owner_id=owner_id))
    context = {
        "form": form,
        "ssh_key": ssh_key
    }
    return render(request, "team/ssh_keys/manage.html", context=context)