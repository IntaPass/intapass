from django.shortcuts import render, redirect, resolve_url

from .models import Host
from .forms import HostForm

def hosts_list(request):
    hosts = Host.objects.all()
    context = {
        "hosts": hosts
    }
    return render(request, "hosts/index.html", context=context)

def create_host(request):
    form = HostForm((request.POST or None))
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(resolve_url("hosts:index"))
    context = {
        "form": form
    }
    return render(request, "hosts/create.html", context=context)

def manage_host(request, pk=None):
    host = Host.objects.get(pk=pk)
    form = HostForm((request.POST or None), instance=host)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(resolve_url("hosts:index"))
    context = {
        "host": host,
        "form": form
    }
    return render(request, "hosts/manage.html", context=context)