import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

# print(response.json())
# print(response.status_code)
# print(response.headers["Content-Type"])

#rechtstreeks keyword value uit json halen
#print(response.json()['title'])

#response omzetten naar woordenboek en keyword value eruit halen
json_res = response.json()
print(json_res['title'])
print(json_res)

check = json_res['completed']

if check == True:
    print("Goed gedaan")
else:
    print("Er moet nog werk gebeuren")



