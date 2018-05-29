from django.conf.urls import url
from .import views
from django_filters.views import FilterView
from .filters import *
#This is the url linker
urlpatterns =[
    url(r'^$',views.College_list,name='College_list'),
url(r'^College/(?P<pk>\d+)/$', views.College_detail, name='college_detail'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
url(r'^search/$',FilterView.as_view(filterset_class = CollegeFilter,template_name='Blog/f_list.html') , name='sarch'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^College/(?P<pk>\d+)/comments$', views.add_comment, name='add_comment'),
url(r'^College/(?P<pk>\d+)/comments$', views.edit_comment, name='edit_comment'),
# url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
# url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

url(r'^College/(?P<pk>\d+)/comment$', views.Commenter, name='commenter'),

url(r'^signup/$', views.SignUp.as_view(), name='signup'),


]