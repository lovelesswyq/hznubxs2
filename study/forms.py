# -*- coding: utf-8 -*-
from django import forms

from .models import studyComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = studyComment
        fields = ('name', 'body')
