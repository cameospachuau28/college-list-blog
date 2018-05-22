from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import PostForm
from django.shortcuts import redirect
from .filters import *

def College_list(request):
    coll= College.objects.all()
    return render(request, 'Blog/post_list.html', {'coll': coll})

def College_detail(request, pk):
    collw = get_object_or_404(College, pk=pk)
    return render(request, 'blog/post_detail.html', {'collw': collw})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)


            post.save()
            return redirect('college_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

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
    return render(request, 'blog/post_edit.html', {'form': form})

def sarch(request):
    Coll_list = College.objects.all()
    COLL_filter = CollegeFilter(request.GET, queryset=Coll_list)
    return render(request, 'blog/f_list.html', {'filter': COLL_filter})

def contact(request):
    return render(request,'blog/Contact.html',{})