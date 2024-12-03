import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate('main/firebase/serviceAccountKey.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'groovify-ugb.firebasestorage.app'
    })
else:
    firebase_admin.initialize_app(cred, name='unique-app-name')

db = firestore.client()

bucket = storage.bucket()

