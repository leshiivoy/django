from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import slugify

menu =[
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Судак', 'content': 'Среда обитания судака', 'is_published': True},
    {'id': 2, 'title': 'Налим', 'content': 'Среда обитания налима', 'is_published': True},
    {'id': 3, 'title': 'Плотва', 'content': 'Среда обитания плотвы', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'fishing/index.html', context=data)


def about(request):
    return render(request, 'fishing/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
