from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    context = {
        "products": product_objects
    }

    return render(request=request, template_name='product/index.html', context=context)


