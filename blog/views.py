from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def insertPost(request):
    posts = Post.objects.all()
    posts = Post.objects.filter(state=True)

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('/')    
    context = {'form':form,'posts':posts}
    return render (request, 'index.html',context)

def post(request, pk):
	post = Post.objects.get(id=pk)
	context = {'post':post}
	return render(request, 'post.html', context)

def editPost(request, pk):
    post =  Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect ('/')    
    context = {'form':form}
    return render (request, 'index.html',context)