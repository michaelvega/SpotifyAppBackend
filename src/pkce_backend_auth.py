import pkce
from urllib.parse import urlencode

code_verifier, code_challenge = pkce.generate_pkce_pair()

client_id = '7124ee1288704e86ae5f719c1c308a96'
redirect_uri = 'http://localhost:5001'
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
