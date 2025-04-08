from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    product_objects = Product.objects.all()

    # Search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None and not 'clear' in request.POST:
        product_objects = product_objects.filter(name__icontains=item_name)

    #Paginator code
    
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    context = {
        "products": product_objects
    }


    return render(request=request, template_name='product/index.html', context=context)


def detail(request, prod_id):
    print("ZOHAIB TESTING")
    item = Product.objects.get(id=prod_id) or None
    context = {"product": item}

    return render(request=request,template_name='product/detail.html', context=context)

def checkout(request):
    return render(request=request, template_name="product/checkout.html", context={})


