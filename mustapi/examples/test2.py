import requests

url = "http://127.0.0.1:8000/devs/bT1ycZ1U"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Response:", response.json())
