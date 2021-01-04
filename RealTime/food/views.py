from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class IndexClassView(ListView):
    model = Item
    template_name='food/index.html'
    context_object_name ='item_list'


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


class detail(DetailView):
    model = Item
    template_name='food/detail.html'

class create_item(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'food.add_item'

    model = Item
    fields = ['item_name','item_desc','item_image','item_opening_hours','item_shipping','item_shipping_available','item_sales','item_allowed_people','item_people_inside']
    template_name='food/item_form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def update_item(request,id):
    item = Item.objects.get(id=id)

    if item.user_name.get_username == request.user.get_username:
        form = ItemForm(request.POST or None,instance=item)

        if form.is_valid():
            form.save()
            return redirect('food:index')

        return render(request,'food/item_form.html',{'form':form,'item':item})
    else:
        return HttpResponse('<h1>You have no permission to edit this item</h1>')

def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if item.user_name.get_username == request.user.get_username:
        if request.method == 'POST':
            item.delete()
            return redirect('food:index')
        
        return render(request,'food/item_delete.html',{'item':item})
    else:
        return HttpResponse('<h1>You have no permission to delete this item</h1>')