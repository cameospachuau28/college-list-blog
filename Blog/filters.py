from django import forms
from .models import College
import django_filters





class CollegeFilter(django_filters.FilterSet):
    College_name = django_filters.CharFilter(name='College_name',lookup_expr='contains')
    Total_seats= django_filters.DateFilter(name='Total_seats',lookup_expr='lte')
    #Clss = django_filters.CharFilter(name='CLASS_CHOICE')
    class Meta:
        model = College
        fields = ['College_name', 'Courses_offered']