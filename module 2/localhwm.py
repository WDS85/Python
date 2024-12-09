import requests

api_url = "http://localhost:8085/data.json"
response = requests.get(api_url)
result = response.json()

if response.status_code == 200:
    print(result)


