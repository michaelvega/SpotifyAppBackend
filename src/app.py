from flask import Flask, jsonify
import requests

app = Flask(__name__)


def getAuthHeader(token):
    return {"Authorization": "Bearer " + token}


@app.route('/api/userInfo/<token>', methods=['GET'])
def get_playlists(token):
    url = "https://api.spotify.com/v1/me"
    headers = getAuthHeader(token)

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