
from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

SPOTIPY_CLIENT_ID = '4d710772416d4105aa262d74f50d8125'
SPOTIPY_CLIENT_SECRET = 'f86716776d824a13a44a5611a4648ddf'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback/'
# Add your desired scope
SCOPE = 'user-read-currently-playing'

# Set up Spotify OAuth
sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope=SCOPE)

@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    return "Access token retrieved successfully!"

if __name__ == "__main__":
    app.run(debug=True)
