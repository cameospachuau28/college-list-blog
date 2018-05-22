from django import forms

from .models import College

class PostForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ('College_name', 'Courses_offered',)