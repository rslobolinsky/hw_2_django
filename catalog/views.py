from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.

def home(request):
    categories = Category.objects.all()[:4]
    context = {
        'object_list': categories,
        'title_1': 'Фрукты - Овощи Магаз',
        'title_2': 'Фрукты - Овощи Магаз - это отличный вариант покупки фруктов и овощей онлайн',
    }
    return render(request, 'catalog/home.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'object_list': categories,
        'title_1': 'Категории',
        'title_2': 'Все категории товаров',
    }
    return render(request, 'catalog/category.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    products = Product.objects.filter(pk=pk)
    context = {
        'object_list': products,
        'title_1': f'Категория {category_item}',
        'title_2': f'{category_item.description}',
    }
    return render(request, 'catalog/product.html', context)


def product(request, pk):
    prod = Product.objects.get(pk=pk)
    context = {
        'object': prod,
        'title_1': f'{prod.name}',
        'title_2': f'Категория {prod.category}',
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')
