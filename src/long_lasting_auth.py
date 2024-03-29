"""
Use this if we can store client secret.

client_secret is left as blank in order to push to github; we should get it from some secure storage, instead of hard coding it in.

Token is printed in callback() - should be stored in the future.

In request_authorization(), modify scope according to what permissions are needed; reference below
https://developer.spotify.com/documentation/web-api/concepts/scopes
"""
import base64
from urllib.parse import urlencode
from flask import Blueprint, request
import requests

long_auth = Blueprint('long_auth', __name__, )

client_id = '7124ee1288704e86ae5f719c1c308a96'
client_secret = ''
redirect_uri = 'http://localhost:5001/api/long_auth/'


def encode_to_base64(id, secret):
    # Concatenate client_id and client_secret with a colon
    combined_str = id + ':' + secret

    # Convert the combined string to bytes
    combined_bytes = combined_str.encode('utf-8')

    # Encode the bytes to base64
    encoded_bytes = base64.b64encode(combined_bytes)

    # Convert the encoded bytes back to a string
    encoded_string = encoded_bytes.decode('utf-8')

    return encoded_string

"""
GET request to the /authorize endpoint
"""
def request_authorization():
    request_url = 'https://accounts.spotify.com/authorize'
    scope = 'user-read-private user-read-email user-top-read'

    params = {
        'client_id': client_id,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': redirect_uri
    }

    encoded_params = urlencode(params)

    auth_url_with_params = f"{request_url}?{encoded_params}"

    print("Redirect user to:", auth_url_with_params)

"""
POST request to the /api/token endpoint
"""
@long_auth.route('/', methods=['GET'])
def callback():
    auth_code = request.args.get('code')
    request_url = 'https://accounts.spotify.com/api/token'
    params = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + encode_to_base64(client_id, client_secret)
    }

    response = requests.post(request_url, params=params, headers=headers)
    print(response.json()['access_token'])
    return "Success"


if __name__ == '__main__':
    request_authorization()