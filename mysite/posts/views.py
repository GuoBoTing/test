from urllib.parse import quote_plus
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

# Create your views here.
def post_home(request):
	return render(request, 'resume.html')


def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, 'post_form.html', context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	share_string = quote_plus(instance.content)
	context = {
		"title": "Detail",
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	queryset = Post.objects.all().order_by('-timestamp')
	paginator = Paginator(queryset, 10)
	
	page = request.GET.get('page')
	page_objects = paginator.get_page(page)
	context = {
		"title": "List",
		"objects_list": queryset,
		"page_objects": page_objects
	}
	return render(request, 'post_list.html', context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.Files or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form
	}
	return render(request, 'post_form.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect('list')