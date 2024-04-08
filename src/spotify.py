from flask import Flask, jsonify
import requests
from llm import llm_api

app = Flask(__name__)
app.register_blueprint(llm_api, url_prefix="/api/llm")

def getAuthHeader(token):
    return {"Authorization" : "Bearer " + token}



@app.route('/api/userInfo/<token>', methods = ['GET'])
def get_userInfo(token):
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

@app.route('/api/userID/<token>', methods = ['GET'])
def get_userID(token):
    url = "https://api.spotify.com/v1/me"
    headers = getAuthHeader(token)
    
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        data = data["id"]
        # Extract and return the username
        return jsonify(data)
    else:
        # Print error message if request fails
        print(f"Failed to get user info: {response.text}")
        return None
    

@app.route('/api/userPlaylists/<token>', methods = ['GET'])
def get_userPlaylists(token):
    
    temp = "https://api.spotify.com/v1/me"
    print(getAuthHeader(token))
    headers = getAuthHeader(token)
    response = requests.get(temp, headers=headers)
    userData = response.json()
    userID = userData["id"]

    url = f'https://api.spotify.com/v1/users/{userID}/playlists'
    headers = getAuthHeader(token)
    
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        

        return jsonify(data["items"])
    else:
        # Print error message if request fails
        print(f"Failed to get user playlists: {response.text}")
        return None
    

@app.route('/api/userTopArtists/<token>', methods = ['GET'])
def get_userTopArtists(token):

    url = f'https://api.spotify.com/v1/me/top/artists'
    headers = getAuthHeader(token)
    
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        

        return jsonify(data["items"])
    else:
        # Print error message if request fails
        print(f"Failed to get user topArtists: {response.text}")
        return None
    

@app.route('/api/userTopTracks/<token>', methods = ['GET'])
def get_userTopTracks(token):

    url = f'https://api.spotify.com/v1/me/top/tracks'
    headers = getAuthHeader(token)
    
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        

        return jsonify(data["items"])
    else:
        # Print error message if request fails
        print(f"Failed to get user topArtists: {response.text}")
        return None



if __name__ == '__main__':
    # Run the Flask application on port 5001 (for example)
    app.run(debug=True, port=5001)
