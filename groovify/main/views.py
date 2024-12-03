import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_admin import auth, storage
from .firebase import db

# Vista de la página principal
def index(request):
    return render(request, 'index.html')

# Vista para registrar un nuevo usuario
def register_user_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')

        try:
            # Crear usuario en Firebase y guardar datos en Firestore
            user = auth.create_user(email=email, password=password)
            db.collection('users').document(user.uid).set({
                'name': name,
                'email': email,
                'uid': user.uid,
                'type': 'user'
            })
            return redirect('login')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/register_user.html')

# Vista para iniciar sesión
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Verificar las credenciales del usuario
            user = auth.get_user_by_email(email)
            request.session['email'] = email
            return redirect('home_user')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'web/login.html')

# Vista principal para el usuario autenticado
def home_user(request):
    email = request.session.get('email', None)
    query = request.GET.get('query', '').lower()

    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix='music/')
    song_urls = []

    for index, blob in enumerate(blobs):
        if index > 0:
            song_url = blob.generate_signed_url(expiration=datetime.timedelta(minutes=60), method='GET')
            song_name = blob.name.lower()
            if query in song_name:
                song_urls.append(song_url)

    return render(request, 'web/home_user.html', {'song_urls': song_urls, 'query': query, 'email': email})

# Vista para cerrar sesión
def logout_view(request):
    request.session.flush()
    return redirect('login')
