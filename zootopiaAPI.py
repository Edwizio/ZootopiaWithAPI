import requests
import json

def load_API_date():
    """
    This function reads data from an API and loads through the get function in
    requests module.
    """
    name = 'fox'
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'Gyfnk0yFcglo+i9JYnYu6Q==0gk5md4xfMsblhcH'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        #print(json.dumps(data, indent=4, sort_keys=True))
        return data
    else:
        return "Error:", response.status_code, response.text

def read_HTML(file_path):
  """ Reads the data from the HTML file"""
  with open(file_path, "r", encoding="utf-8") as handle:
    return handle.read()
