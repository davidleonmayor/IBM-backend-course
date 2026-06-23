import requests
import json

BASE_URL = "http://localhost:8000/api/"

print("Testing Django login/signup API...")

# Test signup
print("\n1. Testing signup...")
signup_data = {
    "names": "David",
    "last_names": "Leon",
    "email": "david@test.com",
    "password": "1234"
}

signup_response = requests.post(
    BASE_URL + "signup/",
    json=signup_data
)

print(f"Signup status: {signup_response.status_code}")
if signup_response.status_code == 201:
    print(f"Signup response: {signup_response.json()}")
    user = signup_response.json()
else:
    print(f"Signup error: {signup_response.text}")

# Test login
print("\n2. Testing login...")
login_data = {
    "email": "david@test.com",
    "password": "1234"
}

login_response = requests.post(
    BASE_URL + "login/",
    json=login_data
)

print(f"Login status: {login_response.status_code}")
if login_response.status_code == 200:
    print(f"Login response: {login_response.json()}")
else:
    print(f"Login error: {login_response.text}")

print("\nDone!")
