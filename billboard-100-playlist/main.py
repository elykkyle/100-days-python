from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
current_user = sp.me()["id"]
user_date = input("Which date do you want to get music from? Enter as YYYY-MM-DD: ")
year = int(user_date.split("-")[0])

top_100_url = f"https://billboard.com/charts/hot-100/{user_date}"
print(top_100_url)

response = requests.get(top_100_url)
top_100_page = response.text

soup = BeautifulSoup(top_100_page, 'html.parser')

song_titles_extract = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s")
song_titles = [title.getText().strip() for title in song_titles_extract]
song_uris = []

for title in song_titles:
    try:
        q = f"track:{title} year:{year}"
        search_results = sp.search(q=q, type="track")
        song_uri = search_results["tracks"]["items"][0]["uri"]
    except IndexError:
        year -= 1
        try:
            q = f"track:{title} year:{year}"
            search_results = sp.search(q=q, type="track")
            song_uri = search_results["tracks"]["items"][0]["uri"]
        except IndexError:
            continue
        else:
            song_uris.append(song_uri)
    else:
        song_uris.append(song_uri)
    print(len(song_uris))

playlist_name = f"Billboard Top 100 for {user_date}"
try:
    playlist = sp.user_playlist_create(current_user, playlist_name, public=False, description="Songs from the Billboard Top 100" )
except Exception as err:
    print(f"Error: {err=}, {type(err)=}")
    raise
playlist_id = playlist["id"]

try:
    sp.playlist_add_items(playlist_id, song_uris)
except Exception as err:
    print(f"Error: {err=}, {type(err)=}")
    raise

print(f"Done! Find your playlist at {playlist['external_urls']['spotify']}")
