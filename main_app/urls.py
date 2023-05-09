from django.urls import path 
from main_app import views 
urlpatterns = [
    path('home/', views.Home, name='home' ),
    path('delete/<int:id>', views.Delete, name='delete'),
    path('edit/<int:id>', views.Edit, name='edit'),
    path('add/', views.Add, name='add'),
    path('seach/', views.Search, name='search'),



    

]
