from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Product, Additions
from .forms import productForm
from order.forms import customLineItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .contexts import additions_contents

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


@user_passes_test(lambda u: u.is_authenticated)
def customize_product(request, item_id):
    """ a view to let user customize products in their order """
    product = get_object_or_404(Product, id=item_id)
    addition_list = Additions.objects.all()
    form = customLineItemForm(instance=request.user)
    additiones = additions_contents(request)
    current_additions = additiones['additions']
    additions_total = additiones['total']

    if request.method == 'POST':
        form = customLineItemForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            form = customLineItemForm()
            return redirect('customize_product')

    if 'addition_dict' in request.session:
        addition_dict = request.session.get('addition_dict')

    context = {
        'addition_list': addition_list,
        'product': product,
        'form': form,
        'current_additions': current_additions,
        'additions_total': additions_total,
        }
    return render(request, 'product/customize_product.html', context)


def addition(request, product_id, item_id):
    if request.method == 'POST':
        addition = get_object_or_404(Additions, id=item_id)
        product = get_object_or_404(Product, id=product_id)
        addition_dict = request.session.get('addition_dict', {})
        quantity = int(request.POST['quantity'])
        redirect_url = request.POST.get('redirect_url')

        if str(addition.name) in addition_dict:
            quantity += addition_dict[str(addition.name)]['quantity']

        addition_dict[str(addition.name)] = {
            'addition_id': addition.id,
            'addition_name': addition.name,
            'quantity': quantity,
        }

        request.session['addition_dict'] = addition_dict
        return redirect(redirect_url)


def delete_addition(request, item_id):
    if request.method == "POST":
        redirect_url = request.POST.get('redirect_url')
        addition = get_object_or_404(Additions, id=item_id)
        addition_dict = request.session.get("addition_dict")
        addition_dict.pop(str(addition.name))
        request.session['addition_dict'] = addition_dict

    return redirect(redirect_url)


def adjust_additions(request, item_id):
    if request.method == "POST":
        addition = get_object_or_404(Additions, id=item_id)
        addition_dict = request.session.get('addition_dict')
        item = addition_dict[str(addition.name)]
        redirect_url = request.POST.get('redirect_url')
        quantity = item['quantity']
        if request.POST.get('increment'):
            item['quantity'] = quantity + 1
        elif request.POST.get('decrement'):
            if quantity == '1':
                addition_dict.pop(str(addition.name))
            else:
                item['quantity'] = quantity - 1

        request.session['addition_dict'] = addition_dict
        return redirect(redirect_url)
