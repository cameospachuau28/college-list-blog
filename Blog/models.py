from django.db import models
from django.utils import timezone


class Course(models.Model):


    name = models.CharField(max_length=200,help_text="Enter the Course Name")
    summary = models.TextField(max_length=200, help_text="Enter brief description",null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    College_name = models.CharField(max_length=200,primary_key=True)
    Location = models.CharField(max_length=200)
    Courses_offered = models.ManyToManyField(Course,help_text="Select Courses")
    Comment = models.TextField()

    def __str__(self):

        return self.College_name


