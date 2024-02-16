# :mortar_board: Wikipedia scraper 
BeCode learning project aiming at scraping wikipedia and using API.

## :bell: Description 
In the project a Wikipedia Scraper object is created. It refers to https://country-leaders.onrender.com and fetches the information about the leaders of the countries. Next, it goes to a Wikipedia page about a leader, and saves the information from the first paragraph of the article. The data is stored in ```.json``` file

## :school_satchel: Installation
:computer: Install Python and all the libraries that are mentioned in the requerements.txt.

## Usage
1. Run the main.py to get the information about every country in the list provided by the API and its leader and save it to the json file. 
2. Customize the usage of the scraper with the following methods:
- `get_countries()` returns a list of the supported countries from the API
- `get_leaders(country: str)` populates the `leader_data` object with the leaders of a country retrieved from the API
- `get_first_paragraph(wikipedia_url: str)` returns the first paragraph (defined by the HTML tag `<p>`) with details about the leader
- `to_json_file(filepath: str)` stores the data structure into a JSON file with the name provided.

## Contributors 
Trainee Alfiya Khabibullina
Coach Vanessa Rivera Quiñones

