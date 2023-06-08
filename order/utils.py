from .models import Product


def perform_search(query):
    results = []
    items = Product.objects.all()
    for item in items:
        if query.lower() in item.name.lower():
            results.append(item)
    return results
