import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register_user(request):
    return render(request, 'web/register_user.html')

def register_artist(request):
    return render(request, 'web/register_artist.html')

def login(request):
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

