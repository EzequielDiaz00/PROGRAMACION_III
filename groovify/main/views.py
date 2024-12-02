import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_admin import auth, firestore
from .firebase import db

def index(request):
    return render(request, 'index.html')

def register_user_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')

        try:
            # Crear usuario en Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password
            )

            # Guardar datos adicionales en Firestore
            db.collection('users').document(user.uid).set({
                'name': name,
                'email': email,
                'uid': user.uid,
                'type': 'user'
            })

            return redirect('login')  # Redirigir al login después de registro

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/register_user.html')

def register_artist_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')

        try:
            # Crear artista en Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password
            )

            # Guardar datos adicionales en Firestore
            db.collection('artist').document(user.uid).set({
                'name': name,
                'email': email,
                'uid': user.uid,
                'type': 'artist'
            })

            return redirect('login')  # Redirigir al login después de registro

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/register_artist.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Verificar las credenciales del usuario en Firebase
            user = auth.get_user_by_email(email)
            # Aquí puedes agregar lógica para validar la contraseña
            # O si estás usando Firebase Admin SDK para login, puedes generar un JWT o similar

            return redirect('home_user')  # Redirigir al home si login es exitoso

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/login.html')

def home_user(request):
    # Ruta a la carpeta de audio
    audio_folder = os.path.join(settings.STATIC_ROOT, 'audio')
    # Obtiene la lista de archivos en la carpeta
    try:
        audio_files = os.listdir(audio_folder)
    except FileNotFoundError:
        audio_files = []

    # Renderiza la plantilla con los archivos de audio
    return render(request, 'web/home_user.html', {'audio_files': audio_files})

def home_artist(request):
    return render(request, 'web/home_artist.html')
