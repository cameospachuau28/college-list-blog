from django.conf.urls import url
from .import views
from django_filters.views import FilterView
from .filters import *
#This is the url linker
urlpatterns =[
    url(r'^$',views.College_list,name='College_list'),
url(r'^College/(?P<pk>[a-zA-Z]+)/$', views.College_detail, name='college_detail'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>[a-zA-Z]+)/edit/$', views.post_edit, name='post_edit'),
url(r'^search/$',FilterView.as_view(filterset_class = CollegeFilter,template_name='Blog/f_list.html') , name='sarch'),
url(r'^contact/$', views.contact, name='contact'),
]