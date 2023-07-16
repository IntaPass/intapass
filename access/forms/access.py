from django import forms

from access.models import Access

class GrantAccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ["host", "ssh_key", "root_access", ]
