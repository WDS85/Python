import requests

print(f"How many jokes do you want to see? ", end="")
amount = int(input())

api_url = (f"https://v2.jokeapi.dev/joke/Any")
response = requests.get(api_url)

try:
    if response.status_code == 200:
        results = response.json()

        if results['type'] == 'single':
            print(results)
        
        else:
            result['type'] == 'twopart':
            print()



except ValueError:
    print("Er werd geen cijfer ingegeven")
