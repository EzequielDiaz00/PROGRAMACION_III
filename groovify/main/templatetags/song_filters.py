from django import template
import urllib.parse

register = template.Library()

@register.filter
def extract_song_name(url):
    """
    Extrae el nombre de la canción desde una URL.
    """
    if not url:
        return "Canción desconocida"
    
    # Quitar los parámetros de la URL (después del "?")
    clean_url = url.split('?')[0]
    
    # Extraer el nombre del archivo (después del último "/")
    file_name = clean_url.split('/')[-1]
    
    # Decodificar caracteres especiales y quitar la extensión
    song_name = urllib.parse.unquote(file_name).replace('.mp3', '').replace('_', ' ')
    
    return song_name


@register.filter
def sort_by_name(songs):
    """
    Ordena las canciones por nombre de canción (después del guion).
    """
    return sorted(songs, key=lambda x: x.split(' - ')[1] if ' - ' in x else x)

@register.filter
def sort_by_artist(songs):
    """
    Ordena las canciones por nombre de artista (antes del guion).
    """
    return sorted(songs, key=lambda x: x.split(' - ')[0] if ' - ' in x else x)
