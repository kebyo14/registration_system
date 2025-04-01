from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact3
from .models import Nav

# Create
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile_image = request.FILES.get('profile_image')

        # Проверка пароля
        if password != confirm_password:
            return render(request, 'create_item.html', {'error_message': 'Passwords do not match'})

        # Проверка существующего пользователя
        if Contact3.objects.filter(email=email).exists():
            return render(request, 'create_item.html', {'error_message': 'Email already registered'})

        # Сохраняем изображение
        file_url = None
        if profile_image:
            fs = FileSystemStorage(location='media/profile_pics')  # Папка хранения
            filename = fs.save(profile_image.name, profile_image)
            file_url = f'profile_pics/{filename}'

        # Создаём пользователя
        user = Contact3(name=name, email=email, password=password, profile_image=file_url)
        user.save()

        # Сохраняем в сессии
        request.session['user_name'] = user.name
        request.session['user_image'] = f'/media/{user.profile_image}' if user.profile_image else None

        return redirect('index')  # После регистрации перебрасываем на index.html

    return render(request, 'create_item.html')

   


users = {
    "testuser": {
        "password": "1234",
        "profile_image": "/media/profile_pics/testuser.jpg"
    }
}

def link_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        try:
            user = Contact3.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_name'] = user.name
                request.session['user_image'] = f'/media/{user.profile_image}' if user.profile_image else None
                return redirect('index')
            else:
                return render(request, 'link_item.html', {'error_message': 'Invalid password'})
        except Contact3.DoesNotExist:
            return render(request, 'link_item.html', {'error_message': 'User not found'})

    return render(request, 'link_item.html')

   

def logout(request):
    request.session.flush()
    return redirect('index')







# Добавляем обработчик для index.html
def index(request):
    navs = Nav.objects.all()
    return render(request, 'index.html', {'navs' : navs})  
# Update
def update_item(request, item_id):
    item = get_object_or_404(Contact3, id=item_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm_password')
        item.name = name
        item.email = email
        item.password = password
        item.password1 = password1
        item.save()
        return redirect('link_item')

    return render(request, 'update_item.html', {'item': item})


# Delete



def base(request):
    items = Contact3.objects.all()  
    return render(request, 'base.html', {'items': items})  


from .forms import ContactForm
from django.contrib import messages  # Для уведомлений

from django.http import JsonResponse
from .models import Forms  # Импортируем новую модель
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def save_contact(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            phone = data.get("phone")

            if not name or not phone:
                return JsonResponse({"error": "Все поля обязательны!"}, status=400)

            Forms.objects.create(name=name, phone=phone)

            return JsonResponse({"message": "Данные успешно сохранены!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Неверный формат данных!"}, status=400)

    return JsonResponse({"error": "Только POST-запросы разрешены!"}, status=405)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Forms

@csrf_exempt
def save_form(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        phone = data.get("phone")

        if name and phone:
            Forms.objects.create(name=name, phone=phone)
            return JsonResponse({"success": True})
        
        return JsonResponse({"success": False, "error": "Заполните все поля!"})
    
    return JsonResponse({"error": "Неверный метод запроса"}, status=400)