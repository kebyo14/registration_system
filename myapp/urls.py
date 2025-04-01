from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import save_form
from .views import save_contact

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('signup/', views.create_item, name='create_item'),  # Регистрация
    path('signin/', views.link_item, name='link_item'),  # Вход
    path('logout/', views.logout, name='logout'),
    path("save_form/", save_form, name="save_form"),

 path('save_contact/', save_contact, name='save_contact'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('base/', views.base, name='base'),
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
