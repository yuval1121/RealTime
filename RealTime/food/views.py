from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
# Create your views here.

class IndexClassView(ListView):
    model = Item;
    template_name='food/index.html'
    context_object_name ='item_list'


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
        }

    return render(request,'food/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
        
    return render(request,'food/item_delete.html',{'item':item})