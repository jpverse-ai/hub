"""Clase: Fundamentos de OOP con un Mini-Spotify (Marc Anthony).

Objetivo:
- Explicar clases e instancias.
- Diferenciar atributos vs metodos.
- Entender __init__ y self.
- Construir un mini sistema con Song, Playlist, User, Player y SpotifyApp.
"""


class Song:
    def __init__(self, song_id, title, artist, album, year, genre, duration_sec):
        # Atributos (datos/estado)
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.genre = genre
        self.duration_sec = duration_sec

        # Estado que cambia con el uso
        self.is_playing = False
        self.likes = 0
        self.plays = 0

    # Metodos (acciones)
    def play(self):
        self.is_playing = True
        self.plays += 1
        return f"▶️ Reproduciendo: {self.title} — {self.artist} (plays: {self.plays})"

    def pause(self):
        self.is_playing = False
        return f"⏸️ Pausada: {self.title}"

    def like(self):
        self.likes += 1
        return f"❤️ Like: {self.title} (likes: {self.likes})"

    def info(self):
        mins = self.duration_sec // 60
        secs = self.duration_sec % 60
        return (
            f"🎵 {self.title} — {self.artist}\n"
            f"Album: {self.album} | Year: {self.year} | Genre: {self.genre}\n"
            f"Duration: {mins}:{secs:02d} | Likes: {self.likes} | Plays: {self.plays}"
        )


class Playlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []  # lista de objetos Song

    def add_song_unique(self, song):
        for s in self.songs:
            if s.song_id == song.song_id:
                return f"✅ '{song.title}' ya esta en '{self.name}'"
        self.songs.append(song)
        return f"➕ Agregada '{song.title}' a '{self.name}'"

    def list_songs(self):
        if len(self.songs) == 0:
            return f"'{self.name}' esta vacia."
        lines = [f"🎶 Playlist: {self.name} (owner: {self.owner})"]
        for i, song in enumerate(self.songs, start=1):
            lines.append(f"{i}. {song.title} — {song.artist} ({song.genre})")
        return "\n".join(lines)

    def total_duration(self):
        total = 0
        for song in self.songs:
            total += song.duration_sec
        mins = total // 60
        secs = total % 60
        return f"⏱️ Duracion total: {mins}:{secs:02d}"


class User:
    def __init__(self, username):
        self.username = username
        self.liked_songs = []
        self.playlists = []

    def like_song(self, song):
        for s in self.liked_songs:
            if s.song_id == song.song_id:
                return f"✅ {self.username} ya habia dado like a '{song.title}'"
        self.liked_songs.append(song)
        song.like()
        return f"❤️ {self.username} liked '{song.title}'"

    def create_playlist(self, name):
        playlist = Playlist(name, self.username)
        self.playlists.append(playlist)
        return playlist

    def show_library(self):
        if len(self.liked_songs) == 0:
            return f"📚 {self.username} aun no tiene likes."
        lines = [f"📚 Liked songs de {self.username}:"]
        for i, song in enumerate(self.liked_songs, start=1):
            lines.append(f"{i}. {song.title} — {song.artist} (likes: {song.likes})")
        return "\n".join(lines)


class Player:
    def __init__(self):
        self.current_song = None

    def play_song(self, song):
        if self.current_song is not None and self.current_song.is_playing:
            self.current_song.pause()
        self.current_song = song
        return song.play()

    def pause(self):
        if self.current_song is None:
            return "⚠️ No hay cancion cargada."
        return self.current_song.pause()

    def now_playing(self):
        if self.current_song is None:
            return "🔇 Nada sonando."
        state = "sonando" if self.current_song.is_playing else "en pausa"
        return f"🎧 {state}: {self.current_song.title} — {self.current_song.artist}"


class SpotifyApp:
    def __init__(self):
        self.catalog = {}
        self.users = {}
        self.player = Player()

    def add_song_to_catalog(self, song):
        self.catalog[song.song_id] = song
        return f"✅ '{song.title}' agregada al catalogo."

    def show_catalog(self):
        if len(self.catalog) == 0:
            return "📦 Catalogo vacio."
        lines = ["📦 Catalogo de canciones:"]
        for song in self.catalog.values():
            lines.append(
                f"- {song.title} — {song.artist} | plays={song.plays} | likes={song.likes}"
            )
        return "\n".join(lines)

    def find_songs_by_artist(self, artist_name):
        found = []
        for song in self.catalog.values():
            if song.artist.lower() == artist_name.lower():
                found.append(song)
        return found

    def find_song_by_title(self, title):
        for song in self.catalog.values():
            if song.title.lower() == title.lower():
                return song
        return None

    def register_user(self, username):
        if username in self.users:
            return self.users[username]
        user = User(username)
        self.users[username] = user
        return user

    def play_by_id(self, song_id):
        song = self.catalog.get(song_id)
        if song is None:
            return f"⚠️ No existe song_id: {song_id}"
        return self.player.play_song(song)

    def top_songs_by_plays(self, n=3):
        songs = list(self.catalog.values())
        songs.sort(key=lambda s: s.plays, reverse=True)
        return songs[:n]


def demo():
    app = SpotifyApp()

    vivir = Song("ma_001", "Vivir Mi Vida", "Marc Anthony", "3.0", 2013, "Salsa", 252)
    valio = Song("ma_002", "Valio la Pena", "Marc Anthony", "Valio la Pena", 2004, "Salsa", 276)
    ahora = Song("ma_003", "Ahora Quien", "Marc Anthony", "Amar Sin Mentiras", 2004, "Pop/Salsa", 260)

    app.add_song_to_catalog(vivir)
    app.add_song_to_catalog(valio)
    app.add_song_to_catalog(ahora)
    print(app.show_catalog())

    user = app.register_user("Jhon")

    mix = user.create_playlist("Marc Anthony Essentials")
    mix.add_song_unique(vivir)
    mix.add_song_unique(valio)
    mix.add_song_unique(valio)

    print(mix.list_songs())
    print(mix.total_duration())

    app.play_by_id("ma_001")
    app.play_by_id("ma_001")
    app.play_by_id("ma_002")

    print(app.player.now_playing())

    user.like_song(vivir)
    user.like_song(vivir)
    print(user.show_library())

    songs_ma = app.find_songs_by_artist("Marc Anthony")
    print("🎤 Encontradas:", [s.title for s in songs_ma])

    top = app.top_songs_by_plays(n=2)
    print("🔥 Top:", [(s.title, s.plays) for s in top])

    print(app.show_catalog())


if __name__ == "__main__":
    demo()
