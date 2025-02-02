from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('signup\/', views.create_item, name='create_item'),  # Регистрация
    path('signin/', views.link_item, name='link_item'),  # Вход
    path('logout/', views.logout_view, name='logout'),

    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('base/', views.base, name='base'),
]
