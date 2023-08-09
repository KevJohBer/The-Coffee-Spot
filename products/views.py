"""
Products App - Views

views for products app
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from order.forms import CustomLineItemForm
from .models import Product, Additions, Rating
from .forms import ProductForm, RatingForm
from .contexts import additions_contents

# Create your views here.


# Admin product management
@user_passes_test(lambda u: u.is_superuser)
def create_product(request):
    """ A view for admin to create products """

    form = ProductForm()
    context = {
        'form': form
        }

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        category_names = ['Regular', 'Special', 'Premium']
        category_name = category_names[category_id - 1]
        form = ProductForm(data=request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.category = category_name
            product.save()
            return redirect('home_page')
        messages.error(request, 'data invalid, check your \
            information and try again')

    return render(request, 'product/create_product.html', context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, item_id):
    """ deletes a product """
    product = get_object_or_404(Product, id=item_id)
    product.delete()
    return redirect('order')


@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, item_id):
    """ A view to allow superuser to edit product infomation """
    product = get_object_or_404(Product, id=item_id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        category_id = int(request.POST.get('category_id'))
        category_names = ['Regular', 'Special', 'Premium']
        category_name = category_names[category_id - 1]
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            edited_product = form.save(commit=False)
            edited_product.category = category_name
            edited_product.save()
            return redirect('order')

    context = {
        'form': form,
        'product': product,
        }
    return render(request, 'product/edit_product.html', context)


@user_passes_test(lambda u: u.is_authenticated)
def product_details(request, item_id):
    """ A view to get more information about the product and rate it """
    product = get_object_or_404(Product, id=item_id)
    form = RatingForm()
    rating_values = [1, 2, 3, 4, 5]
    if request.method == 'POST':
        redirect_url = request.POST.get('redirect_url')
        if Rating.objects.filter(user=request.user, product=product).exists():
            rating = Rating.objects.filter(
                user=request.user, product=product)[0]
            rating.rating = request.POST['rating']
            rating.save()
            return redirect(redirect_url)
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()
            return redirect(redirect_url)
        form = RatingForm()
    context = {
        'product': product,
        'form': form,
        'rating_values': rating_values,
    }
    return render(request, 'product/product_details.html', context)


@user_passes_test(lambda u: u.is_authenticated)
def customize_product(request, item_id):
    """ a view to let user customize products in their order """
    product = get_object_or_404(Product, id=item_id)
    addition_list = Additions.objects.all()
    form = CustomLineItemForm(instance=request.user)
    additions = additions_contents(request)
    current_additions = additions['additions']
    additions_total = additions['total']
    if request.method == 'POST':
        form = CustomLineItemForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('order')
        form = CustomLineItemForm()
        return redirect('customize_product')

    context = {
        'addition_list': addition_list,
        'product': product,
        'form': form,
        'current_additions': current_additions,
        'additions_total': additions_total,
        }
    return render(request, 'product/customize_product.html', context)


# Additions


@user_passes_test(lambda u: u.is_authenticated)
def addition(request, item_id):
    """ adds an addition to customized drink """
    if request.method == 'POST':
        addition_dict = request.session.get('addition_dict', {})
        quantity = int(request.POST['quantity'])
        redirect_url = request.POST.get('redirect_url')

        if item_id in list(addition_dict.keys()):
            addition_dict[item_id] += quantity
        else:
            addition_dict[item_id] = quantity

        request.session['addition_dict'] = addition_dict
    return redirect(redirect_url)


@user_passes_test(lambda u: u.is_authenticated)
def delete_addition(request, item_id):
    """ Deletes selected addition from customized drink"""
    if request.method == "POST":
        redirect_url = request.POST.get('redirect_url')
        addition_dict = request.session.get("addition_dict")
        addition_dict.pop(item_id)
        request.session['addition_dict'] = addition_dict

    return redirect(redirect_url)


@user_passes_test(lambda u: u.is_authenticated)
def adjust_additions(request, item_id):
    """ adjust chosen additions for custom drink"""
    if request.method == "POST":
        addition_dict = request.session.get('addition_dict')
        redirect_url = request.POST.get('redirect_url')
        if request.POST.get('increment'):
            addition_dict[item_id] += 1
        elif request.POST.get('decrement'):
            if addition_dict[item_id] == 1:
                addition_dict.pop(item_id)
            else:
                addition_dict[item_id] -= 1

        request.session['addition_dict'] = addition_dict
    return redirect(redirect_url)
