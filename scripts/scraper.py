import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a requestt o the website
url = "https://theivycollection.com/restaurants/"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the restaurant containers
restaurants = soup.find_all("a", class_="restarant-tile")

# Step 4: Extract and clean the data
data = []
for r in restaurants:
    name = r.find("h3").text.strip() if r.find("h3") else "No name"
    location = r.find("p").text.strip() if r.find("p") else "No location"
    data.append({"name": name, "location": location})

# Step 5: Convert to CSV
df = pd.DataFrame(data)
df.to_csv("ivy_restaurants.csv", index=False)