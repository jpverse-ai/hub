# Clase 01 - Prework Python (OOP Mini-Spotify)

Esta clase introduce Programacion Orientada a Objetos con un mini sistema tipo Spotify.

## Objetivos
- Entender clases e instancias.
- Diferenciar atributos vs metodos.
- Usar `__init__` y `self` correctamente.
- Conectar objetos en un sistema simple.

## Estructura de la clase
- `notebooks/`: notebook con teoria y codigo.
- `codigo/`: scripts y ejercicios.
- `planes_clase/`: planes de clase en Markdown.
- `assets/`: documentos base (DOCX).

## Diagrama de clases

```mermaid
classDiagram
  class Song {
    +song_id
    +title
    +artist
    +album
    +year
    +genre
    +duration_sec
    +play()
    +pause()
    +like()
    +info()
  }
  class Playlist {
    +name
    +owner
    +songs
    +add_song_unique()
    +list_songs()
    +total_duration()
  }
  class User {
    +username
    +liked_songs
    +playlists
    +like_song()
    +create_playlist()
    +show_library()
  }
  class Player {
    +current_song
    +play_song()
    +pause()
    +now_playing()
  }
  class SpotifyApp {
    +catalog
    +users
    +player
    +add_song_to_catalog()
    +show_catalog()
    +find_songs_by_artist()
    +find_song_by_title()
    +register_user()
    +play_by_id()
    +top_songs_by_plays()
  }

  Playlist --> Song : contiene
  User --> Playlist : crea
  User --> Song : da like
  SpotifyApp --> Player : usa
  SpotifyApp --> Song : registra
  SpotifyApp --> User : registra
```

## Flujo de la app

```mermaid
flowchart LR
  A[Crear app] --> B[Agregar canciones]
  B --> C[Registrar usuario]
  C --> D[Crear playlist]
  D --> E[Reproducir]
  E --> F[Dar like]
  F --> G[Top canciones]
```

## Archivos clave
- Notebook: `notebooks/clase.ipynb`
- Script base: `codigo/clase.py`
