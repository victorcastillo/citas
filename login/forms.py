from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(required=True, error_messages = {'required': "Tu email es requerido."})
	password = forms.CharField(required=True, widget=forms.PasswordInput(), error_messages = {'required': "El password."})