from . import views
from django.urls import path

app_name='food'
urlpatterns = [
    #//
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/1
    path('<int:pk>/',views.detail.as_view(),name='detail'),
    #/item/
    path('item/',views.item,name='item'),
    #add items
    path('add/',views.create_item.as_view(),name='create_item'),
    #edit items
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]

