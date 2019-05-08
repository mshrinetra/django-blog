from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

from .models import BlogPost
from .forms import NewBlogForm, NewBlogModelForm


@login_required
def blog_update_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = NewBlogModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        try:
            form.save()
            context = {'header': 'Update success!!'}
        except:
            context = {'header': 'Update Filed!!'}
        return render(request, 'blog/new.html', context)
    else:
        context = {
            'header': 'Update the Post',
            'form': form
        }
        return render(request, 'blog/new.html', context)


@login_required
def blog_del_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    try:
        obj.delete()
        context = {'header': 'Delete Success'}
    except:
        context = {'header': 'Delete Failed'}
    return render(request, 'blog/view.html', context)


def blog_list_page(request):
    qs = BlogPost.objects.all()
    if qs.count() >= 1:
        objs = qs

    context = {'objs': objs,
               'header': 'All Blogs'}

    return render(request, 'blog/list.html', context)


def blog_view_page(request, slug):
    query_set = BlogPost.objects.filter(slug=slug)
    if query_set.count() != 1:
        raise Http404
    obj = query_set.first()

    context = {'obj': obj,
               'header': 'Viewing Blog'}
    return render(request, 'blog/view.html', context)

# add login url to decorater as @login_required(login_url='/login')
# OR add in setting as LOGIN_URL = '/login'
@login_required
def blog_new_page(request):
    form = NewBlogModelForm(request.POST or None)
    if form.is_valid():
        try:
            # form.save()  # If no modification is required
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            context = {'header': 'New post success!!'}
        except:
            context = {'header': 'New post Filed!!'}
        form = NewBlogModelForm()
        return render(request, 'blog/new.html', context)
    else:
        context = {
            'header': 'Create New Post',
            'form': form
        }
        return render(request, 'blog/new.html', context)
