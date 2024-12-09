import requests

#https://v2.jokeapi.dev/joke/Any

print(f"How many jokes do you want to see? ", end="")
amount = int(input())

api_url = (f"https://v2.jokeapi.dev/joke/Any?amount={amount}")
response = requests.get(api_url)

# try:
#     if response.status_code == 200:
#         results = response.json()
#         for result in results:
#             print(result)

#         print(parts)
#         if parts == "single":
#             print(result['joke'])
#         else:
#             parts == "twopart"
#             print(result['setup'])
#             print(result['delivery'])
    
#     else:
#         print(f'Fout: {response.status_code}')

# except ValueError:
#     print("Er werd geen cijfer ingegeven")

try:
    if response.status_code == 200:
        results = response.json()

        # Check if 'jokes' key exists in the response
        if 'jokes' in results:
            for result in results['jokes']:
                if result['type'] == 'single':  # Joke is a single-line joke
                    print(result['joke'])
                elif result['type'] == 'twopart':  # Joke has two parts (setup and delivery)
                    print(result['setup'])
                    print(result['delivery'])
        else:
            print("No jokes found in the response.")
    else:
        print(f'Error: {response.status_code}')

except ValueError:
    print("Er werd geen cijfer ingegeven")
