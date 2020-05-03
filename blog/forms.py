#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Fernando
#
# Created:     01/05/2020
# Copyright:   (c) Fernando 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
