import firebase_admin
from firebase_admin import credentials, firestore, storage

# Ruta al archivo de credenciales de Firebase
cred = credentials.Certificate('main/firebase/serviceAccountKey.json')

# Inicializar Firebase Admin SDK, asegurándonos de no inicializar más de una vez
if not firebase_admin._apps:
    # Inicialización sin nombre de aplicación si es la primera vez
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'groovify-ugb.firebasestorage.app'
    })
else:
    # Si ya está inicializada, usaremos un nombre único
    firebase_admin.initialize_app(cred, name='unique-app-name')

# Inicializar Firestore
db = firestore.client()

# Inicializar Storage para acceder a Firebase Storage
bucket = storage.bucket()

# Ahora puedes usar `bucket` para interactuar con Firebase Storage
