# -*- coding: utf-8 -*-
from django import forms

from .models import unuseComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = unuseComment
        fields = ('name', 'email', 'body')
