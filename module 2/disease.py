import requests

print("Voer het land in: ", end="")
country = input().strip()

api_url = (f"https://disease.sh/v3/covid-19/countries/{country}?strict=true")
response = requests.get(api_url)


if response.status_code == 200:
    result = response.json()
    cases = result['cases']
    deaths = result['deaths']
    recovered = result['recovered']
    print(f"\nThe country {country} has:")
    print(f"{cases} known Covid-19 cases")
    print(f"{deaths} known Covid-19 deaths")
    print(f"{recovered} known recoveries")
else:
    print(f"Fout: {response.status_code}")

    