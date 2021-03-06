from django import forms
from .models import College,Course
import django_filters





class CollegeFilter(django_filters.FilterSet):
    College_name = django_filters.CharFilter(name='College_name',lookup_expr='icontains')
    Total_seats= django_filters.DateFilter(name='Total_seats',lookup_expr='lte')
    Courses_offered =College.objects.all().order_by('Courses_offered')

    print (Courses_offered)
    #Clss = django_filters.CharFilter(name='CLASS_CHOICE')
    class Meta:
        model = College
        fields = ['College_name', 'Courses_offered']