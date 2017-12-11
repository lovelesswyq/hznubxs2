# -*- coding: utf-8 -*-
from django import forms

from .models import travelComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = travelComment
        fields = ('name', 'email', 'body')
