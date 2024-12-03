class MusicPlayer {
    constructor() {
        this.audio = new Audio();
        this.playlist = [];
        this.currentIndex = 0;
        this.progressBar = document.getElementById('progressbarSong');
        this.volumeControl = document.getElementById('volumeControl');
        this.songInfo = document.getElementById('song_info');
        this.init();
    }

    // Inicializa el reproductor y configura los controles
    init() {
        this.loadPlaylist();
        this.setupControls();
        this.audio.ontimeupdate = () => this.updateProgressBar();
        this.audio.onended = () => this.skipSong();
        this.setupVolumeControl();
    }

    // Configura el control de volumen
    setupVolumeControl() {
        this.volumeControl.addEventListener('input', (e) => {
            this.audio.volume = e.target.value;
        });
    }

    // Carga las canciones en la lista de reproducción
    loadPlaylist() {
        document.querySelectorAll('.song-item').forEach(item => {
            const songUrl = item.dataset.file;
            if (songUrl) {
                this.playlist.push(songUrl);
                item.addEventListener('click', () => {
                    this.currentIndex = this.playlist.indexOf(songUrl);
                    this.playSong();
                });
            }
        });
    }

    // Actualiza la información de la canción actual
    updateSongInfo() {
        const songUrl = this.playlist[this.currentIndex];
        if (songUrl) {
            try {
                const cleanUrl = songUrl.split('?')[0];
                const fileName = cleanUrl.split('/').pop();
                const cleanName = decodeURIComponent(fileName.replace('.mp3', '').replace(/_/g, ' '));
                this.songInfo.innerHTML = `<p>${cleanName}</p>`;
            } catch (error) {
                console.error("Error al procesar el nombre de la canción:", error);
                this.songInfo.innerHTML = `<p>Archivo desconocido</p>`;
            }
        } else {
            this.songInfo.innerHTML = `<p>No hay información disponible</p>`;
        }
    }

    // Reproduce la canción seleccionada
    playSong() {
        const songUrl = this.playlist[this.currentIndex];
        if (songUrl) {
            this.audio.src = songUrl;
            this.audio.play()
                .then(() => this.updateSongInfo())
                .catch(err => console.error("Error reproduciendo canción:", err));
        }
    }

    // Pausa la canción
    pauseSong() {
        this.audio.pause();
    }

    // Detiene la canción y reinicia su tiempo
    stopSong() {
        this.audio.pause();
        this.audio.currentTime = 0;
    }

    // Avanza a la siguiente canción
    skipSong() {
        this.currentIndex = (this.currentIndex + 1) % this.playlist.length;
        this.playSong();
    }

    // Reproduce la canción anterior
    backSong() {
        this.currentIndex = (this.currentIndex - 1 + this.playlist.length) % this.playlist.length;
        this.playSong();
    }

    // Actualiza la barra de progreso mientras la canción se reproduce
    updateProgressBar() {
        if (this.audio.duration) {
            this.progressBar.value = (this.audio.currentTime / this.audio.duration) * 100;
        }
    }

    // Configura los controles del reproductor
    setupControls() {
        document.getElementById('player_play').addEventListener('click', () => this.playSong());
        document.getElementById('player_pause').addEventListener('click', () => this.pauseSong());
        document.getElementById('player_stop').addEventListener('click', () => this.stopSong());
        document.getElementById('player_skip').addEventListener('click', () => this.skipSong());
        document.getElementById('player_back').addEventListener('click', () => this.backSong());
        this.progressBar.addEventListener('input', e => {
            if (this.audio.duration) {
                this.audio.currentTime = (e.target.value / 100) * this.audio.duration;
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', () => new MusicPlayer());
