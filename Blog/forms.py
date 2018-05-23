from django import forms

from .models import College,Commenting

class PostForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ('College_name', 'Courses_offered','Comment')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commenting
        fields = ('name','comment_body',)