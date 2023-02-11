from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import AccountApplication, Materials

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")

    class Meta:
        model = User
        fields = ("username", )


class AccountApplicationForm(forms.ModelForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
	materials_provide = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=Materials.objects.all(),
    )

	class Meta:
		model = AccountApplication
		fields = '__all__'