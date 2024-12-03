class MusicPlayer {
    constructor() {
        this.audio = new Audio();
        this.playlist = [];
        this.currentIndex = 0;
        this.progressBar = document.getElementById('progressbarSong');
        this.volumeControl = document.getElementById('volumeControl'); // Referencia al control de volumen
        this.songInfo = document.getElementById('song_info');
        this.init();
    }

    init() {
        this.loadPlaylist();
        this.setupControls();
        this.audio.ontimeupdate = () => this.updateProgressBar();
        this.audio.onended = () => this.skipSong();
        this.setupVolumeControl(); // Configuración del control de volumen
    }

    setupVolumeControl() {
        this.volumeControl.addEventListener('input', (e) => {
            this.audio.volume = e.target.value; // Ajustar el volumen del audio
        });
    }

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

    playSong() {
        const songUrl = this.playlist[this.currentIndex];
        if (songUrl) {
            this.audio.src = songUrl;
            this.audio.play()
                .then(() => this.updateSongInfo())
                .catch(err => console.error("Error reproduciendo canción:", err));
        }
    }

    pauseSong() {
        this.audio.pause();
    }

    stopSong() {
        this.audio.pause();
        this.audio.currentTime = 0;
    }

    skipSong() {
        this.currentIndex = (this.currentIndex + 1) % this.playlist.length;
        this.playSong();
    }

    backSong() {
        this.currentIndex = (this.currentIndex - 1 + this.playlist.length) % this.playlist.length;
        this.playSong();
    }

    updateProgressBar() {
        if (this.audio.duration) {
            this.progressBar.value = (this.audio.currentTime / this.audio.duration) * 100;
        }
    }

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
