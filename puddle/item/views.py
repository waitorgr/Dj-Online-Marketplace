from django.shortcuts import render,get_object_or_404
from .models import Item


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk) #пошук itema
    related_items=Item.objects.filter(Category=item.Category, is_sold=False).exclude(pk=pk)[0:3] #пошук предмета в одній категорії

    return render(request, 'item/detail.html',{
        'item': item,
        'related_items': related_items
    })
