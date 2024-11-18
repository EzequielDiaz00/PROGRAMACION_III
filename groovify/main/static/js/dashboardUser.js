// Variables globales
let currentIndex = 0;
const audio = new Audio();
const progressBar = document.getElementById('progressbarSong');
const songInfo = document.getElementById('song_info');
let audioContext = null; // Asegurarse de que AudioContext se inicializa correctamente

// Actualiza la información de la canción
function updateSongInfo(index) {
    const songName = playlist[index].split('/').pop();
    songInfo.innerHTML = `<p>${decodeURIComponent(songName.replace('.mp3', ''))}</p>`;
}

// Reproduce la canción actual
function playSong() {
    audio.play().catch(error => {
        console.error("Error al intentar reproducir la canción:", error);
    });
    updateSongInfo(currentIndex);
}

// Cambia la canción al hacer clic en una de la lista
document.addEventListener('DOMContentLoaded', () => {
    if (playlist.length > 0) {
        document.querySelectorAll('.song-item').forEach((item, index) => {
            item.addEventListener('click', () => {
                // Inicializa el AudioContext solo al hacer clic en la canción
                if (!audioContext) {
                    audioContext = new (window.AudioContext || window.webkitAudioContext)();

                    const analyser = audioContext.createAnalyser();
                    const sourceNode = audioContext.createMediaElementSource(audio);
                    sourceNode.connect(analyser);
                    analyser.connect(audioContext.destination);

                    // Filtros Biquad para cada banda
                    const bass = audioContext.createBiquadFilter();
                    const midLow = audioContext.createBiquadFilter();
                    const mid = audioContext.createBiquadFilter();
                    const midHigh = audioContext.createBiquadFilter();
                    const treble = audioContext.createBiquadFilter();

                    // Configuración de los filtros
                    bass.type = 'lowshelf';
                    bass.frequency.value = 250; // Frecuencia de corte para bajos
                    bass.gain.value = 0;

                    midLow.type = 'peaking';
                    midLow.frequency.value = 500; // Frecuencia de corte para medios bajos
                    midLow.Q.value = 1;
                    midLow.gain.value = 0;

                    mid.type = 'peaking';
                    mid.frequency.value = 1000; // Frecuencia de corte para medios
                    mid.Q.value = 1;
                    mid.gain.value = 0;

                    midHigh.type = 'peaking';
                    midHigh.frequency.value = 3000; // Frecuencia de corte para medios altos
                    midHigh.Q.value = 1;
                    midHigh.gain.value = 0;

                    treble.type = 'highshelf';
                    treble.frequency.value = 6000; // Frecuencia de corte para agudos
                    treble.gain.value = 0;

                    // Conectar los filtros
                    bass.connect(midLow);
                    midLow.connect(mid);
                    mid.connect(midHigh);
                    midHigh.connect(treble);
                    treble.connect(analyser);

                    // Ecualizador: Actualiza los valores de los filtros con los controles
                    document.getElementById('bass').addEventListener('input', (e) => {
                        bass.gain.value = parseInt(e.target.value);
                        console.log(`Bass Gain: ${bass.gain.value}`);
                    });

                    document.getElementById('mid-low').addEventListener('input', (e) => {
                        midLow.gain.value = parseInt(e.target.value);
                    });

                    document.getElementById('mid').addEventListener('input', (e) => {
                        mid.gain.value = parseInt(e.target.value);
                    });

                    document.getElementById('mid-high').addEventListener('input', (e) => {
                        midHigh.gain.value = parseInt(e.target.value);
                    });

                    document.getElementById('treble').addEventListener('input', (e) => {
                        treble.gain.value = parseInt(e.target.value);
                    });
                }

                currentIndex = index; // Actualiza el índice
                audio.src = playlist[currentIndex];

                // Solo reproduce la canción después de un clic
                playSong();
            });
        });

        // Carga y reproduce la primera canción cuando el usuario hace clic en "play"
        const playButton = document.getElementById('player_play');
        playButton.addEventListener('click', () => {
            loadFirstSong();
        });
    }
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

// Reproduce la siguiente canción automáticamente cuando termine
audio.onended = () => {
    skipSong();
};

// Actualiza la barra de progreso
audio.ontimeupdate = () => {
    if (audio.duration) {
        progressBar.value = (audio.currentTime / audio.duration) * 100;
    }
};

// Permite cambiar el tiempo de reproducción a través de la barra de progreso
progressBar.addEventListener('input', (e) => {
    audio.currentTime = (e.target.value / 100) * audio.duration;
});

// Controles
document.getElementById('player_play').addEventListener('click', playSong);
document.getElementById('player_pause').addEventListener('click', pauseSong);
document.getElementById('player_stop').addEventListener('click', stopSong);
document.getElementById('player_skip').addEventListener('click', skipSong);
document.getElementById('player_back').addEventListener('click', backSong);

// Carga y reproduce la primera canción
function loadFirstSong() {
    if (playlist.length > 0) {
        audio.src = playlist[0];
        playSong();
    }
}
