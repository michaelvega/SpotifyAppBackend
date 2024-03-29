"""
Use this if we CANNOT preserve details after first authentication securely.

We need to login every time and get a new token.
"""

import pkce
from urllib.parse import urlencode
from flask import Blueprint, request
import requests

pkce_auth = Blueprint('pkce_auth', __name__, )

code_verifier = pkce.generate_code_verifier(length=128)
code_challenge = pkce.get_code_challenge(code_verifier)

client_id = '7124ee1288704e86ae5f719c1c308a96'
redirect_uri = 'http://localhost:5001/api/pkce/'


def send_to_external():
    scope = 'user-read-private user-read-email'

    auth_url = 'https://accounts.spotify.com/authorize'
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'scope': scope,
        'code_challenge_method': 'S256',
        'code_challenge': code_challenge,
        'redirect_uri': redirect_uri,
    }

    encoded_params = urlencode(params)

    auth_url_with_params = f"{auth_url}?{encoded_params}"

    print("Redirect user to:", auth_url_with_params)


def request_token(auth_code):
    request_url = 'https://accounts.spotify.com/api/token'

    params = {
        'client_id': client_id,
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri,
        'code_verifier': code_verifier
    }

    encoded_params = urlencode(params)
    request_url_with_params = f"{request_url}?{encoded_params}"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(request_url_with_params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        token = data['access_token']
        print(token)
    else:
        print(response.text)
        return None


@pkce_auth.route('/', methods=['GET'])
def get_auth_code():
    auth_code = request.args.get('code')
    print("auth code: " + auth_code)
    # if auth_code == '':
    #     return "Token received!"
    request_token(auth_code)
    return "Requested token."


if __name__ == '__main__':
    send_to_external()



