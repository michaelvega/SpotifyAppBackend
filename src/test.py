import requests

# Define the base URL of the Flask API
BASE_URL = 'http://localhost:5001'


def test_username(token):
    url = f'{BASE_URL}/api/userInfo/{token}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Get Personal Info {response} - PASS")
        print(response.json())
    elif response.status_code == 404:
        print(f"Get book by ID FAIL (Book not found)")
    else:
        print(f"Get book by ID FAIL")
        print(f"Error: {response.text}")


if __name__ == '__main__':
    test_username("BQA_C8MIqcryBsLwCdGK28iUx7asG1ymK_SznOUIg6vY8C1qIBcBLw9xNI21jhIqRQ58c1ljfZqah3NPffeqsuc3JTHt3CjzFfMZi2Zj4BbVP_99Tdh13tFfm7Vjh_FTg3TPpUbMga_j-Vaphf4R31PcGUNcyNtQlQ-hwIG4y0-2MCBUajZXCD_EuwWALzaxz-Ajac3iM_XT")