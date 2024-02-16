from scraper import WikipediaScraper
from tqdm import tqdm

print("Scraping the data...")

object = WikipediaScraper()

for country in tqdm(object.get_countries()):
    object.get_leaders(country)

print("Saving the data...")

object.to_json_file("leaders_data.json")

print("Done!")