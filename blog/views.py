from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import Post


menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'categories_selected': 0,
    }

    return render(request, 'blog/index.html', context=context)


def show_category(request, categories_slug):
    posts = Post.objects.filter(slug=categories_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': categories_slug,
    }

    return render(request, 'blog/index.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'categories_selected': post.categories_id,
    }

    return render(request, 'blog/post.html', context=context)



def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'About page'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!<h1>')
