import requests



print("Enter a city: ", end="")
city = input().strip()
api_key = "8e499d31f9bc1e1871876b11ad0dbb7a"
api_url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
response = requests.get(api_url)
result = response.json()

if response.status_code == 200:
    temp = result['main']['temp']
    beschrijving = result['weather'][0]['description']
    vochtigheid = result['main']['humidity']
    windsnelheid = result['wind']['speed']

    print(temp)
    print(beschrijving)
    print(vochtigheid)
    print(windsnelheid)
    
 

# print(result)




