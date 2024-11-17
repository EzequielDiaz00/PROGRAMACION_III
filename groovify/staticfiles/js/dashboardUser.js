// Archivo: main/static/js/player.js

// Lista de canciones (Django genera estas rutas con {% static %})
const playlist = [
    '{% static "audio/song1.mp3" %}',
    '{% static "audio/song2.mp3" %}',
    '{% static "audio/song3.mp3" %}'
];

// Variables para controlar el reproductor
let currentIndex = 0; // Índice de la canción actual
const audio = new Audio(playlist[currentIndex]); // Elemento audio con la primera canción
const progressBar = document.getElementById('progressbarSong');
const songInfo = document.getElementById('song_info');

// Actualiza la información de la canción
function updateSongInfo() {
    const songName = playlist[currentIndex].split('/').pop(); // Obtiene el nombre del archivo
    songInfo.innerHTML = `<p>${decodeURIComponent(songName.replace('.mp3', ''))}</p>`;
}

// Función para reproducir la canción
function playSong() {
    audio.play();
    updateSongInfo();
}

// Función para pausar la canción
function pauseSong() {
    audio.pause();
}

// Función para detener la canción
function stopSong() {
    audio.pause();
    audio.currentTime = 0; // Reinicia la canción
}

// Función para avanzar a la siguiente canción
function skipSong() {
    currentIndex = (currentIndex + 1) % playlist.length; // Cambia al siguiente índice, reinicia al final
    audio.src = playlist[currentIndex];
    playSong();
}

// Función para regresar a la canción anterior
function backSong() {
    currentIndex = (currentIndex - 1 + playlist.length) % playlist.length; // Regresa al anterior
    audio.src = playlist[currentIndex];
    playSong();
}

// Manejo de la barra de progreso
audio.ontimeupdate = () => {
    progressBar.value = (audio.currentTime / audio.duration) * 100; // Actualiza el progreso
};
progressBar.addEventListener('input', (e) => {
    audio.currentTime = (e.target.value / 100) * audio.duration; // Cambia el tiempo de reproducción
});

// Event listeners para los controles
document.getElementById('player_play').addEventListener('click', playSong);
document.getElementById('player_pause').addEventListener('click', pauseSong);
document.getElementById('player_stop').addEventListener('click', stopSong);
document.getElementById('player_skip').addEventListener('click', skipSong);
document.getElementById('player_back').addEventListener('click', backSong);

// Inicializa la información de la primera canción
updateSongInfo();
