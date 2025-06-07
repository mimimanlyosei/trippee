import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

# Step 1: URL to scarape
url = "https://ivycollection.com/locations/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Extract restaurant data
cards = soup.select('.location-img-box')

data = []
for card in cards:
    name_tag = card.select_one('.img-text a')
    name = name_tag.text.strip() if name_tag else "No name"
    link = name_tag["href"] if name_tag and name_tag.has_attr("href") else "No link"
    description_tag = card.select_one('.img-desc')
    # Changing this location logic because it does't actually pull any area data.
    # location = description_tag.text.strip() if description_tag else "No location"

    # New area info logic
    if name.lower().startswith("the ivy"):
        area = name.replace("The Ivy", "").split(",")[0].strip()
    else:
        area = "Unknown"

    # test printing to see what is being extracted
    print("NAME:", name)
    print("DESC:", description_tag)
    print("TEXT:", description_tag.text.strip() if description_tag else "None")
    # Result: description_tag exits but its empty and that's why it doesn't give
    # any info to the area column




    data.append({
        "name": name,
        "area": area if area else "Unknown",
        "url": link
    })

# Step 3: Save to CSV in data folder
output_folder = Path("data")
output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / "all_locations.csv"

df = pd.DataFrame(data, columns=["name", "area", "url"])
df.to_csv(output_path, index=False)

# print(f"✅ Ivy locations saved to {output_path}")