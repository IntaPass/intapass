from django import forms
from django.contrib.auth.models import User, Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name",]

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", ]