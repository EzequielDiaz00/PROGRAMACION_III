// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";
import { getFirestore, getDoc, doc } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js";

// Configuración de Firebase
const firebaseConfig = {
    apiKey: "AIzaSyByhyHJGb2m1XknKGCH5RUvQzIdri5ex9w",
    authDomain: "groovify-ugb.firebaseapp.com",
    projectId: "groovify-ugb",
    storageBucket: "groovify-ugb.firebasestorage.app",
    messagingSenderId: "310040910442",
    appId: "1:310040910442:web:3f87829a87bbb9196d8813"
};

// Inicializa Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();
const db = getFirestore(app);

// Iniciar sesión
const signInArtist = document.getElementById('submitLogin');

signInArtist.addEventListener('click', async (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        // Iniciar sesión con Firebase Auth
        const userCredential = await signInWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;

        console.log("Inicio de sesión exitoso:", user.email);

        // Obtener información del usuario desde Firestore
        const userDoc = await getDoc(doc(db, "artist", user.uid)); // Verificar si es artista

        if (userDoc.exists()) {
            // Es un artista
            console.log("El usuario es un artista:", userDoc.data());
            window.location.href = "/home_artist/";
        } else {
            // Si no está en la colección "artist", verificar en "users"
            const userDocUser = await getDoc(doc(db, "users", user.uid));
            if (userDocUser.exists()) {
                // Es un usuario normal
                console.log("El usuario es un usuario normal:", userDocUser.data());
                window.location.href = "/home_user/";
            } else {
                console.error("Usuario no encontrado en ninguna colección.");
                alert("Hubo un error al identificar el tipo de usuario.");
            }
        }
    } catch (error) {
        console.error("Error al iniciar sesión:", error.code, error.message);
        alert("Error al iniciar sesión: " + error.message);
    }
});
