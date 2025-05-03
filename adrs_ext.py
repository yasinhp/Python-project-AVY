
import pandas as pd
import time
import requests

API_KEY = "****************************"
GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

def get_address(lat, lng):
    """Fetch address using Google Maps API for a given latitude and longitude."""
    params = {
        "latlng": f"{lat},{lng}",
        "key": API_KEY
    }
    response = requests.get(GEOCODE_URL, params=params)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            return results[0].get("formatted_address")
        else:
            return "Address Not Found"
    else:
        return f"Error {response.status_code}"

# Load your CSV file
df = pd.read_csv("filtered_real_estate_data.csv")

# Create address column
addresses = []
for i, row in df.iterrows():
    try:
        address = get_address(row["lat"], row["long"])
        addresses.append(address)
        print(f"{i+1}/{len(df)} done")
        time.sleep(0.1)  # slight delay to avoid rate limits
    except Exception as e:
        print(f"Failed at index {i}: {e}")
        addresses.append("Error")

df["address"] = addresses

# Save new CSV
df.to_csv("real_estate_with_addresses_google.csv", index=False)
print("✅ File saved as 'real_estate_with_addresses_google.csv'")