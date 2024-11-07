from django.shortcuts import render

from .models import Item


def item_list(request):
    """App response to request"""
    items = Item.objects.all()
    return render(request, "hello/index.html", {"items": items})

