from django.http.response import JsonResponse

from api.models import Product, Category

def products(requst):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def products_id(requst, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(product.to_json())

def categories(requst):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def categories_id(requst, category_id):
    try:
        category = Product.objects.get(id=category_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(category.to_json())