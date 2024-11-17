// Variables globales
let currentIndex = 0;
const audio = new Audio();
const progressBar = document.getElementById('progressbarSong');
const songInfo = document.getElementById('song_info');

// Actualiza la información de la canción
function updateSongInfo(index) {
  const songName = playlist[index].split('/').pop();
  songInfo.innerHTML = `<p>${decodeURIComponent(songName.replace('.mp3', ''))}</p>`;
}

// Reproduce la canción actual
function playSong() {
  audio.play();
  updateSongInfo(currentIndex);
}

// Cambia la canción al hacer clic en una de la lista
document.querySelectorAll('.song-item').forEach((item, index) => {
  item.addEventListener('click', () => {
    currentIndex = index; // Actualiza el índice
    audio.src = playlist[currentIndex];
    playSong();
  });
});

// Pausa la canción
function pauseSong() {
  audio.pause();
}

// Detiene la canción
function stopSong() {
  audio.pause();
  audio.currentTime = 0;
}

// Avanza a la siguiente canción
function skipSong() {
  currentIndex = (currentIndex + 1) % playlist.length;
  audio.src = playlist[currentIndex];
  playSong();
}

// Retrocede a la canción anterior
function backSong() {
  currentIndex = (currentIndex - 1 + playlist.length) % playlist.length;
  audio.src = playlist[currentIndex];
  playSong();
}

// Actualiza la barra de progreso
audio.ontimeupdate = () => {
  progressBar.value = (audio.currentTime / audio.duration) * 100;
};

progressBar.addEventListener('input', (e) => {
  audio.currentTime = (e.target.value / 100) * audio.duration;
});

// Controles
document.getElementById('player_play').addEventListener('click', playSong);
document.getElementById('player_pause').addEventListener('click', pauseSong);
document.getElementById('player_stop').addEventListener('click', stopSong);
document.getElementById('player_skip').addEventListener('click', skipSong);
document.getElementById('player_back').addEventListener('click', backSong);
