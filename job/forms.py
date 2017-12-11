# -*- coding: utf-8 -*-
from django import forms

from .models import jobComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = jobComment
        fields = ('name', 'email', 'body')
