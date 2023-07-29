from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Additions
from .forms import productForm
from order.forms import customLineItemForm

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
    product = get_object_or_404(Product, id=item_id)
    return render(request, 'product/product_details.html', {'product': product})


def customize_product(request, item_id):
    """ a view to let user customize products in their order """
    product = get_object_or_404(Product, id=item_id)
    addition_list = Additions.objects.all()
    form = customLineItemForm(instance=request.user)

    if request.method == 'POST':
        form = customLineItemForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            form = customLineItemForm()
            return redirect('customize_product')

    context = {
        'addition_list': addition_list,
        'product': product,
        'form': form
        }
    return render(request, 'product/customize_product.html', context)


def addition(request, item_id):
    cart = request.session.get('cart', {})
    addition = get_object_or_404(Additions, id=item_id)
    additions = []
    addition_dict = {}
    quantity = 1

    additions.append(addition)

    addition_dict[str(addition.name)] = {
        'addition_id': addition.id,
        'addition_name': addition.name,
        'quantity': quantity,
    }

    context = {
        'additions': additions,
        'addition_dict': addition_dict,
    }

    return render(request, 'product/customize_product.html', context)
