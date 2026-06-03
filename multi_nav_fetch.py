import requests
import pandas as pd

codes = [119551, 120503, 118632, 119092, 120841]

for code in codes:
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)
        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(f"data/raw/nav_{code}.csv", index=False)

        print(f"NAV data saved for {code}")

    except Exception as e:
        print(f"Error for {code}: {e}")