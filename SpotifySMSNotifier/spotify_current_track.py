import spotipy
from spotipy.oauth2 import SpotifyOAuth
from send_sms import send_sms
import time

# Spotify credentials
SPOTIPY_CLIENT_ID = '4d710772416d4105aa262d74f50d8125'
SPOTIPY_CLIENT_SECRET = 'f86716776d824a13a44a5611a4648ddf'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'

# Spotify OAuth2 Authentication
auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI,
                            scope='user-read-currently-playing')
sp = spotipy.Spotify(auth_manager=auth_manager)

def check_for_artist_and_send_sms(target_artist, message):
    current_track = sp.current_user_playing_track()
    if current_track is not None and current_track['is_playing']:
        artist_name = current_track['item']['artists'][0]['name']
        track_name = current_track['item']['name']
        print(f"Currently playing: {track_name} by {artist_name}")  # Print current track info
        if artist_name.lower() == target_artist.lower():
            send_sms(message)
            print("SMS sent!")  # Confirmation of SMS sent

if __name__ == "__main__":
    target_artist = 'Taylor Swift'
    custom_message = 'RAYAN IS BUMPIN T SWIFT RN ‼️' 

    while True:
        check_for_artist_and_send_sms(target_artist, custom_message)
        time.sleep(1) 
