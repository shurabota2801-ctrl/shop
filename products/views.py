from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def products_list(request, slug_category=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category = None

    if slug_category:
            category = get_object_or_404(Category, slug=slug_category)
            products = Product.objects.filter(category=category, available=True)
    print(f"Запрос: {request}, Метод: {request.method}, сессия: {request.session.items()}")
    return render(request, 'products/products_list.html', 
                  {'products': products,
                   'categories': categories,
                   'category': category
                   })

def products_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    print(f"Детали товара: {request}, {id}, {slug}")
    return render(request, 'products/product_detail.html', {
         'product': product
    })


