from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required

from access.models import Access
from access.forms import GrantAccessForm

@login_required
def index(request):
    """
    Access entries
    """
    entries = Access.objects.all()

    context = {
        "entries": entries
    }
    return render(request, "access/index.html", context=context)

@login_required
def create_access(request):
    form = GrantAccessForm((request.POST or None))

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(resolve_url("access:index"))
    context = {
        "form": form
    }
    return render(request, "access/create.html", context=context)

