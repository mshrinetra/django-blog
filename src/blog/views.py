from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

from .models import BlogPost


def blog_list_page(request):
    qs = BlogPost.objects.all()
    if qs.count() >= 1:
        objs = qs

    context = {"objs": objs,
               "header": "All Blogs"}

    return render(request, "blog/list.html", context)


def blog_view_page(request, slug):
    query_set = BlogPost.objects.filter(slug=slug)
    if query_set.count() != 1:
        raise Http404
    obj = query_set.first()

    context = {"obj": obj,
               "header": "Viewing Blog"}
    return render(request, "blog/view.html", context)


def blog_new_page(request):
    context = {"header": "Create new post"}
    return render(request, "blog/new.html", context)
