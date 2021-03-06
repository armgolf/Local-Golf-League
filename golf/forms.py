from django import forms
from django.forms import ModelForm
from .models import Payment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class PNumber(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('name', 'email', 'phone',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Golfer name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Golfer email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Golfer phone'}),
        }
