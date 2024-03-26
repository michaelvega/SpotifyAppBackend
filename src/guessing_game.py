"""
Game to be embedded into wrapped.

Guess most listened to artist and song.

Guess the artist that appeared in the most playlists.
"""
from flask import jsonify, Blueprint
from utils import get_auth_header
import requests

games = Blueprint('games', __name__, )
"""
Need to decide whether to send request to spotify API or to Firebase for this.

Need PKCE Flow to get the right token: https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow

API docs for top artist/song: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks

API docs for getting playlists: https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists

API docs for getting items from playlist: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks

Test client ID: 7124ee1288704e86ae5f719c1c308a96
Test client secret: saved as local env variable
"""


def get_top_items(token, type):
    url = f"https://api.spotify.com/v1/me/top/{type}"

    headers = get_auth_header(token)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Extract and return top songs
        return jsonify(data)
    else:
        # Print error message if request fails
        print(f"Failed to get user info: {response.text}")
        return None


@games.route('/guessing/songs/<token>', methods=['GET'])
def get_top_songs(token):
    get_top_items(token, "tracks")


@games.route('/guessing/artists/<token>', methods=['GET'])
def get_top_artists(token):
    get_top_items(token, "artists")


if __name__ == '__main__':
    token = ""
    get_top_songs(token)
    get_top_artists(token)