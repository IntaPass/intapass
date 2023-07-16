from django.shortcuts import render

from .models import Access

def index(request):
    """
    Access entries
    """
    entries = Access.objects.all()

    context = {
        "entries": entries
    }
    return render(request, "access/index.html", context=context)