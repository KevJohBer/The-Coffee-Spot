from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Product
from .forms import productForm

# Create your views here.


# Admin product management
@user_passes_test(lambda u: u.is_superuser)
def create_product(request):
    """ A view for admin to create products """

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        category_names = ['Regular', 'Special', 'Premium']
        category_name = category_names[category_id - 1]
        form = productForm(data=request.POST)

        if form.is_valid():
            product = form.save()
            product.category = category_name
            product.save()
            return redirect('home_page')
        else:
            form = productForm()
            errormsg = 'data did not validate'
            context = {'form': form, 'errormsg': errormsg}
            return render(request, 'product/create_product.html', context)

    else:
        form = productForm()
        context = {
            'form': form
            }

        return render(request, 'product/create_product.html', context)

@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, item_id):
    """ deletes a prduct """
    product = get_object_or_404(Product, id=item_id)
    product.delete()
    return redirect('order')

@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, item_id):
    """ A view to allow superuser to edit product infomation """
    product = get_object_or_404(Product, id=item_id)

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        category_names = ['Regular', 'Special', 'Premium']
        category_name = category_names[category_id - 1]
        form = productForm(data=request.POST, instance=product)
        if form.is_valid():
            edited_product = form.save()
            edited_product.category = category_name
            edited_product.save()
            return redirect('order')

    form = productForm(instance=product)
    context = {'form': form}
    return render(request, 'product/edit_product.html', context)


def product_details(request, item_id):
    """ A view to get more information about the product """
    return render(request, 'product/product_details.html')


def customize_product(request, item_id):
    """ a view to let user customize products in their order """
    return render(request, 'product/customize_product.html')
