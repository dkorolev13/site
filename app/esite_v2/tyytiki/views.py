from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import *

menu = [{'title': 'Серьги'},
        {'title': 'Воротники'},
        {'title': 'Подвески'},
        {'title': 'Броши'}
        ]


def index(request):
    prods = Product.objects.all()
    cats = Category.objects.all()
    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Главная страница'}

    return render(request, 'tyytiki/index.html', context=context)


def about(request):
    return render(request, 'tyytiki/about.html', {'menu': menu, 'title': 'О авторе'})


def show_prod(request, prod_id):
    return HttpResponse(f'<h1>Product</h1><p>{prod_id}</p>')


def show_category(request, cat_id):
    prods = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Отображение по рубрикам',
               'cat_selected': cat_id}

    return render(request, 'tyytiki/index.html', context=context)


def all_products(request):
    prods = Product.objects.all()
    cats = Category.objects.all()
    context = {'prods': prods,
               'cats': cats,
               'menu': menu,
               'title': 'Отображение по рубрикам'}

    return render(request, 'tyytiki/products.html', context=context)


# def all_products(request, cat_id):
#     prods = Product.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     context = {'prods': prods,
#                'cats': cats,
#                'menu': menu,
#                'title': 'Отображение по рубрикам',
#                'cat_selected': cat_id}
#
#     return render(request, 'tyytiki/products.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
