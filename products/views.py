from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Product
import json

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        description = data.get('description', '').strip()
        price = data.get('price', 0)

        if not name or price <= 0:
            return JsonResponse({'error': 'Invalid input'}, status=400)

        product = Product.objects.create(name=name, description=description, price=price)
        return JsonResponse({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_products(request):
    products = Product.objects.all().values('id', 'name', 'description', 'price')
    return JsonResponse(list(products), safe=False)


# Create your views here.
def index(request):
    return render(request, 'index.html')
