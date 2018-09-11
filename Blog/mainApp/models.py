from django.db import models
from django import forms

from news.models import Articles

class PostForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'post',)