from django import forms

from .models import Access

class GrantAccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ["host", "ssh_key", "root_access", ]
