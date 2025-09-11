import requests
import json

def load_API_date():
    """
    This function reads data from an API and loads through the get function in
    requests module.
    """
    name = input("Enter a name of an animal: ")
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


def serialize_animal(animal):
  """ This function serializes the whole data to be presented in the HTML

  """
  HTML_text = ""
  try:
    # Appending data to the HTML string
    HTML_text += '<li class="cards__item">'
    HTML_text += f'<div class="card__title"> {animal["name"]}<br/></div>\n'
    HTML_text += '<div class="card__text">'
    HTML_text += '<ul>'
    HTML_text += f"<li class = 'card__points' ><strong> Diet: </strong> {animal["characteristics"]["diet"]}</li>\n"

    HTML_text += f"<li class = 'card__points' ><strong>Location: </strong> {animal["locations"][0]}</li>\n"
    if "type" in animal["characteristics"]:
      HTML_text += f"<li class = 'card__points' ><strong>Type: </strong> {animal["characteristics"]["type"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Kingdom: </strong> {animal["taxonomy"]["kingdom"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Scientific Name: </strong> {animal["taxonomy"]["scientific_name"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Life Span: </strong> {animal["characteristics"]["lifespan"]}</li>\n"
    HTML_text += '</ul>'
    HTML_text += '</div>'
    HTML_text += "</li>\n"

  except KeyError:
    HTML_text += "\n"

  return HTML_text


def serialize_animal(animal):
  """ This function serializes the whole data to be presented in the HTML

  """
  HTML_text = ""
  try:
    # Appending data to the HTML string
    HTML_text += '<li class="cards__item">'
    HTML_text += f'<div class="card__title"> {animal["name"]}<br/></div>\n'
    HTML_text += '<div class="card__text">'
    HTML_text += '<ul>'
    HTML_text += f"<li class = 'card__points' ><strong> Diet: </strong> {animal["characteristics"]["diet"]}</li>\n"

    HTML_text += f"<li class = 'card__points' ><strong>Location: </strong> {animal["locations"][0]}</li>\n"
    if "type" in animal["characteristics"]:
      HTML_text += f"<li class = 'card__points' ><strong>Type: </strong> {animal["characteristics"]["type"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Kingdom: </strong> {animal["taxonomy"]["kingdom"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Scientific Name: </strong> {animal["taxonomy"]["scientific_name"]}</li>\n"
    HTML_text += f"<li class = 'card__points' ><strong>Life Span: </strong> {animal["characteristics"]["lifespan"]}</li>\n"
    HTML_text += '</ul>'
    HTML_text += '</div>'
    HTML_text += "</li>\n"

  except KeyError:
    HTML_text += "\n"

  return HTML_text

def main():
  """
  This is the main function where the functions will be called and executed.
  """

  # Loading the animal's data from the API-ninja using requests module
  animals_data = load_API_date()

  old_HTML = read_HTML("animals_template.html")

  # to store the HTML text
  HTML_output = ""

  # To generate the display info from the json file
  for animal in animals_data:
    HTML_output += serialize_animal(animal)

  # Replacing the animal info is the old HTML Template
  new_HTML = old_HTML.replace("__REPLACE_ANIMALS_INFO__", HTML_output)

  # Creating a new HTML file with the new HTML text
  with open("animals.html", "w") as animal_HTML:
    animal_HTML.write(new_HTML)

  # Printing the successful website generation message
  print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
  main()