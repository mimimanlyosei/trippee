import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Step 1: URL to scarape
url = "https://ivycollection.com/locations/"
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify() [:3000]) # print the first 1000 charachters

# Step 2: Extract restaurant data
# restaurant_cards = soup.find_all("a", class_="location-img-box")
cards = soup.select('.location-img-box')

data = []
for card in cards:
    name_tag = card.select_one('.img-text a')
    name = name_tag.text.strip() if name_tag else "No name"
    link = name_tag["href"] if name_tag and name_tag.has_attr("href") else "No link"
    description_tag = card.select_one('.img-desc')
    location = description_tag.text.strip() if description_tag else "No location"

    print(name, location, link)
    data.append({
        "name": name,
        "location": location,
        "url": link
    })

# Step 3: Save to CSV in data folder
output_folder = os.path.join("data")
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, "ivy_locations.csv")
df = pd.DataFrame(data)
df.to_csv(output_path, index=False)

print(f"✅ Ivy locations saved to {output_path}")