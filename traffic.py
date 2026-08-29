import os
import requests
import logging
from dotenv import load_dotenv
from datetime import datetime
import csv

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/traffic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

now = datetime.now()
if now.weekday() >= 5:
    print("Weekend — no data collected.")
    logging.info("Weekend — no data collected.")
    exit()

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API_KEY")

url = "https://routes.googleapis.com/directions/v2:computeRoutes"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key,
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters"
}

data = {
    "origin": {
        "address": "Prestige Falcon City, Bengaluru, Karnataka, India"
    },
    "destination": {
        "address": "Iblur Lake, Bengaluru, Karnataka, India"
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE_OPTIMAL"
}

response = requests.post(
    url,
    headers=headers,
    json=data
)


route = response.json()["routes"][0]

duration_seconds = int(route["duration"].replace("s", ""))
duration_minutes = duration_seconds / 60

date = now.strftime("%Y-%m-%d")
day = now.strftime("%A")
time = now.strftime("%H:%M")

file_path = "data/traffic_data.csv"

file_exists = os.path.exists(file_path)

with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["date", "day", "time", "travel_minutes"])

    writer.writerow([
        date,
        day,
        time,
        round(duration_minutes, 1)
    ])

print(f"Date: {date}")
print(f"Day: {day}")
print(f"Time: {time}")
print(f"Travel time: {duration_minutes:.1f} minutes")
print("Data saved successfully!")
logging.info("Data saved successfully!")