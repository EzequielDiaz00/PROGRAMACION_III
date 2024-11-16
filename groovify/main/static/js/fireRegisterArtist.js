// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-auth.js";
import { getFirestore, setDoc, doc } from "https://www.gstatic.com/firebasejs/11.0.2/firebase-firestore.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyByhyHJGb2m1XknKGCH5RUvQzIdri5ex9w",
    authDomain: "groovify-ugb.firebaseapp.com",
    projectId: "groovify-ugb",
    storageBucket: "groovify-ugb.firebasestorage.app",
    messagingSenderId: "310040910442",
    appId: "1:310040910442:web:3f87829a87bbb9196d8813"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Registro Artistas
const signUpArtist = document.getElementById('submitRegisterArtist');

signUpArtist.addEventListener('click', (event) => {
    event.preventDefault();

    const emailArtist = document.getElementById('emailArtist').value;
    const passArtist = document.getElementById('passArtist').value;
    const nameArtist = document.getElementById('nameArtist').value;

    const auth = getAuth();
    const dbFire = getFirestore(app);

    createUserWithEmailAndPassword(auth, emailArtist, passArtist)
        .then(async (userCredential) => {
            const user = userCredential.user;

            // Firestore
            await setDoc(doc(dbFire, "artist", user.uid), {
                name: nameArtist,
                email: emailArtist,
                uid: user.uid,
                type: "artist"
            });

            console.log("Artista guardado en Firestore!");

            window.location.href = "/login/";
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.error("Error: ", errorCode, errorMessage);
        });
});
