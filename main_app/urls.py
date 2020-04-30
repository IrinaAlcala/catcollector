from django.urls import path
from . import views
urlpatterns = [
    path('',                      views.home,                name='home'),
    path('about/',                views.about,               name='about'),
    path('cats/',                 views.CatList.as_view(),   name='cats_index'),
    path('cats/<int:pk>/',        views.cat_detail,          name='cats_detail'),
    path('cats/create/',          views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
]