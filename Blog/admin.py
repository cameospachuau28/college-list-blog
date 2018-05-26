from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(College)
#admin.site.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_filter = ['name']
    ordering = ['name']
admin.site.register(Course,CourseAdmin)
admin.site.register(Commenting)