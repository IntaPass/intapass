from django import forms

from access.models import Access, SSHKeys

class GrantAccessForm(forms.ModelForm):
    class Meta:
        model = Access
        fields = ["host", "ssh_key", "root_access", ]

class SSHKeysForm(forms.ModelForm):
    class Meta:
        model = SSHKeys
        fields = ["label", "pub_key", ]