from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):


    name = models.CharField(max_length=200,help_text="Enter the Course Name")
    summary = models.TextField(max_length=200, help_text="Enter brief description",null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    id = models.IntegerField(primary_key=True)
    College_name = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Courses_offered = models.ManyToManyField(Course,help_text="Select Courses")
    Comment = models.TextField()

    def __str__(self):

        return self.College_name
    class Meta:
        ordering =['College_name']


class Commenting(models.Model):
    pot = models.ForeignKey('College',on_delete=models.SET_NULL,null=True,related_name='comments')
    name = models.CharField(max_length=50)
    comment_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def approve(self):
        self.active = True
        self.save()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.pot)

