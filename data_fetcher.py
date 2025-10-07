import os
import requests
from dotenv import load_dotenv

# Loading the API_Key from the .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """


  api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

  if response.status_code == requests.codes.ok:
    data = response.json()
    return data

  else:
    print(f"Error: {response.status_code, response.text}")
    return []