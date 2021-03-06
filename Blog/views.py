from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import PostForm,CommentForm
from django.shortcuts import redirect
from .filters import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

def College_list(request):
    coll= College.objects.all()
    return render(request, 'Blog/post_list.html', {'coll': coll})

def College_detail(request, pk):
    collw = get_object_or_404(College, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit =False)
            comment.collw =collw
            comment.save()
            return redirect('college_detail',pk=pk)
    else:
        form = CommentForm()
    return render(request, 'Blog/post_detail.html', {'collw': collw})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('college_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Blog/post_create.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(College, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)


            post.save()
            return redirect('college_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog/post_edit.html', {'form': form})

def sarch(request):
    Coll_list = College.objects.all()
    COLL_filter = CollegeFilter(request.GET, queryset=Coll_list)
    return render(request, 'Blog/f_list.html', {'filter': COLL_filter})

def contact(request):
    return render(request,'Blog/Contact.html',{})

def add_comment(request,pk):
    post = get_object_or_404(College,pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit =False,instance=post)
            comment.post =post
            comment.save()
            return redirect('college_detail',pk=pk)
    else:
        form = CommentForm()

    return render(request,'Blog/add_comment_to.html',{'form':form},{'pk':post})


def edit_comment(request,pk):
    post = get_object_or_404(College,pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit =False)
            comment.post =post
            comment.save()
            return redirect('college_detail',pk=pk)
    else:
        form = CommentForm()

    return render(request,'Blog/add_comment_to.html',{'form':form},{'pk':post})

# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Commenting, pk=pk)
#     comment.approve()
#     return redirect('college_detail', pk=comment.pk)
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Commenting, pk=pk)
#     comment.delete()
#     return redirect('college_detail', pk=comment.pk)

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def Commenter(request,pk):
    print("POST")

    flight = College.objects.get(id=pk)
    request.session['id'] = flight.pk
    collw = get_object_or_404(Commenting, pk=pk)
    if request.method == 'POST':
        co = Commenting()

        co.name = request.POST['coname']
        co.comment_body = request.POST['cobody']
        # co.created = request.POST['cocreated']
        co.active = request.POST['coactive']
        co.save()
        return redirect('college_detail', pk=collw.pk)
        # context = {'co': co}
        # return render(request, 'Blog/commenter.html', context)
    else:
        id=collw.pk
        return render(request, 'Blog/commenter.html',{'id':id})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Blog/signup.html'



