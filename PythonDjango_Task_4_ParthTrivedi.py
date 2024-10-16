# Code written by Parth Trivedi -

import requests
import pandas as pd

# it will get all cities in India and save into a .CSV file.
def fetch_and_save_indian_cities():
    # API URL that provides cities names.
    api_endpoint = "https://countriesnow.space/api/v0.1/countries/cities"

    request_payload = {"country": "India"}

    try:
        response = requests.post(api_endpoint, json=request_payload)
        response.raise_for_status()
        cities = response.json().get('data', [])
        city_dataframe = pd.DataFrame(cities, columns=["City"])
        city_dataframe.to_csv("indian_cities.csv", index=False)
        print("The list of Indian cities has been saved to 'indian_cities.csv'.")

    except requests.exceptions.RequestException as api_error:
        print(f"An error occurred while fetching cities: {api_error}")

fetch_and_save_indian_cities()