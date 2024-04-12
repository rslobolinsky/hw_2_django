from django.shortcuts import render

from catalog.models import Category


# Create your views here.

def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title_1': 'Фрукты - Овощи Магаз',
        'title_2': 'Фрукты - Овощи Магаз - это отличный вариант покупки фруктов и овощей онлайн'
    }
    return render(request, 'catalog/home.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {
        'object_list': categories,
        'title_1': 'Категории',
        'title_2': 'Все категории товаров'
    }

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')

