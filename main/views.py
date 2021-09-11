from django.shortcuts import render, get_object_or_404

from .models import WishList

def index(request):
    if request.method == 'POST':
        return render(request, 'about2.html', {})
    else:
        return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {'Title': "Whishlist | About page"})


def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk=pk)
    return render(request, 'wish_list.html', {'wishlist':wishlist, 'is_owner_list': wishlist.owner == request.user})