from django.shortcuts import render,redirect
from .models import BlogPost, Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
# Create your views here.


def blogView(request):
    template_name = "blog/blogs.html"
    search_post = request.GET.get('search')
    if search_post:
        quary = Q(Q(title__icontains=search_post) | Q(content__icontains=search_post) | Q(category__title=search_post))
        posts = BlogPost.objects.filter(quary)
    else:
        posts = BlogPost.objects.all().order_by("-create_at")
    categorys= Category.objects.all()
    recent_posts = BlogPost.objects.all().order_by('-create_at')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(4)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts, 
        'categorys': categorys,
        'recent_posts':recent_posts
        }
    return render(request, template_name, context)


def blogDetailsView(request, slug):
    template_name = "blog/blog_details.html"
    details = BlogPost.objects.get(slug=slug)
    categorys = Category.objects.all()
    recent_posts = BlogPost.objects.all().order_by('-create_at')
    context = {
        'details': details,
        'categorys': categorys,
        'recent_posts':recent_posts
    }
    return render(request, template_name, context)



def filterByCategory(request, id):
    template_name = "blog/blogs.html"
    posts = BlogPost.objects.filter(category=id)
    categorys= Category.objects.all()
    recent_posts = BlogPost.objects.all().order_by('-create_at')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,1)
    print(paginator)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts, 
        'categorys': categorys,
        'recent_posts':recent_posts
        }
    return render(request, template_name, context)



