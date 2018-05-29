from django import forms
from django.contrib.auth.models import User

from .models import College,Commenting

class PostForm(forms.ModelForm):

    class Meta:
        model = College
        fields = ('id','College_name','Location', 'Courses_offered','Comment')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commenting
        fields = ('pot','name','comment_body','active')


def clean_username(self):

    username = self.cleaned_data["username"]
    try:
        User.objects.get(username=username)
    except User.DoesNotExist:
        return username
    raise forms.ValidationError(("A user with that username already exists."))