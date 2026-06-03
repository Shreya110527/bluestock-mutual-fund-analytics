import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv("data/raw/live_nav_125497.csv", index=False)

print("Live NAV saved successfully")