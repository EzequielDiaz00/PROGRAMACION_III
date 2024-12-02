import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('main/firebase/serviceAccountKey.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
else:
    firebase_admin.initialize_app(cred, name='unique-app-name')  # Asigna un nombre único si ya está inicializada una app

# Inicializar Firestore
db = firestore.client()
