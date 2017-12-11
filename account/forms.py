# -*- coding: utf-8 -*-

from django import forms
	    
class LoginForm(forms.Form):        
	username = forms.CharField(label='名称')        
	password = forms.CharField(label='暗号',widget=forms.PasswordInput)

from django.contrib.auth.models import User
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='暗号',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入暗号',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
