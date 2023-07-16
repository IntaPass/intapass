from django.shortcuts import render

from .models import Access
from .forms import GrantAccessForm

def index(request):
    """
    Access entries
    """
    entries = Access.objects.all()

    context = {
        "entries": entries
    }
    return render(request, "access/index.html", context=context)

def create_access(request):
    form = GrantAccessForm((request.POST or None))

    if request.method == "POST":
        if form.is_valid():
            form.save()
    context = {
        "form": form
    }
    return render(request, "access/create.html", context=context)