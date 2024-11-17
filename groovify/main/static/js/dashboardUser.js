// Variables globales
let currentIndex = 0; // Índice de la canción actual
const audio = new Audio(playlist[currentIndex]); // Inicializa el reproductor con la primera canción
const progressBar = document.getElementById('progressbarSong');
const songInfo = document.getElementById('song_info');

// Actualiza la información de la canción
function updateSongInfo() {
  const songName = playlist[currentIndex].split('/').pop(); // Obtiene el nombre del archivo
  songInfo.innerHTML = `<p>${decodeURIComponent(songName.replace('.mp3', ''))}</p>`;
}

// Reproduce la canción actual
function playSong() {
  audio.play();
  updateSongInfo();
}

// Pausa la canción
function pauseSong() {
  audio.pause();
}

// Detiene la canción y reinicia el tiempo
function stopSong() {
  audio.pause();
  audio.currentTime = 0;
}

// Avanza a la siguiente canción
function skipSong() {
  currentIndex = (currentIndex + 1) % playlist.length; // Incrementa el índice con reinicio
  audio.src = playlist[currentIndex];
  playSong();
}

// Retrocede a la canción anterior
function backSong() {
  currentIndex = (currentIndex - 1 + playlist.length) % playlist.length; // Decrementa el índice con reinicio
  audio.src = playlist[currentIndex];
  playSong();
}

// Sincroniza la barra de progreso
audio.ontimeupdate = () => {
  progressBar.value = (audio.currentTime / audio.duration) * 100;
};

// Permite cambiar manualmente la posición
progressBar.addEventListener('input', (e) => {
  audio.currentTime = (e.target.value / 100) * audio.duration;
});

// Configura los eventos de los controles
document.getElementById('player_play').addEventListener('click', playSong);
document.getElementById('player_pause').addEventListener('click', pauseSong);
document.getElementById('player_stop').addEventListener('click', stopSong);
document.getElementById('player_skip').addEventListener('click', skipSong);
document.getElementById('player_back').addEventListener('click', backSong);

// Inicializa la información de la primera canción
updateSongInfo();
