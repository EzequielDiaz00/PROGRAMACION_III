import datetime
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_admin import auth, firestore, storage
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

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Verificar las credenciales del usuario en Firebase
            user = auth.get_user_by_email(email)

            # Almacenar el correo electrónico en la sesión
            request.session['email'] = email

            return redirect('home_user')  # Redirigir al home si login es exitoso

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/login.html')


def home_user(request):
    # Obtener el correo electrónico de la sesión
    email = request.session.get('email', None)

    # Obtener el término de búsqueda de la solicitud GET
    query = request.GET.get('query', '').lower()

    # Obtener el bucket de almacenamiento
    bucket = storage.bucket()

    # Obtener todos los blobs en la carpeta 'music/'
    blobs = bucket.list_blobs(prefix='music/')

    # Lista para almacenar las URLs de las canciones
    song_urls = []

    # Recorre los blobs (archivos) en el bucket
    for index, blob in enumerate(blobs):
        if index > 0:  # Omite el primer blob
            song_url = blob.generate_signed_url(expiration=datetime.timedelta(minutes=60), method='GET')
            song_name = blob.name.lower()  # Convierte el nombre de la canción a minúsculas para comparación
            # Filtra según el término de búsqueda
            if query in song_name:
                song_urls.append(song_url)

    # Pasa la lista de URLs, el término de búsqueda y el correo al contexto
    return render(request, 'web/home_user.html', {'song_urls': song_urls, 'query': query, 'email': email})

def logout_view(request):
    # Limpiar la sesión del usuario
    request.session.flush()
    # Redirigir al usuario a la página de inicio de sesión o la página principal
    return redirect('login')
