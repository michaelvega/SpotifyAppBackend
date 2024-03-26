from flask import Flask, jsonify
from utils import get_auth_header
from guessing_game import games
import requests

app = Flask(__name__)
app.register_blueprint(games, url_prefix="/api")

@app.route('/api/userInfo/<token>', methods=['GET'])
def get_playlists(token):
    url = "https://api.spotify.com/v1/me"
    headers = get_auth_header(token)

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the username
        return jsonify(data)
    else:
        # Print error message if request fails
        print(f"Failed to get user info: {response.text}")
        return None


if __name__ == '__main__':
    # Run the Flask application on port 5001 (for example)
    app.run(debug=True, port=5001)