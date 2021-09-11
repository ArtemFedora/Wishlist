from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import WishList
from .forms import ProductForm


def index(request):
    if request.method == 'POST':
        return render(request, 'about2.html', {})
    else:
        return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {'Title': "Whishlist | About page"})


def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        product = form.save()
        wishlist.products.add(product)
        wishlist.save()

    elif request.method == 'GET':
        form = ProductForm()

    return render(
        request,
        'wish_list.html',
        {
            'wishlist': wishlist,
            'is_owner_list': wishlist.owner == request.user,
            'form': form
        }
    )
