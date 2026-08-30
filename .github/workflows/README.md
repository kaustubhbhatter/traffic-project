# Traffic Data Collector

A simple Python project that collects traffic-aware travel times between two locations at specific times on weekdays.

The data is collected using the Google Routes API and stored over time for later traffic trend analysis.

## How it works

    GitHub Actions
          ↓
    Runs traffic.py
          ↓
    Calls Google Routes API
          ↓
    Gets travel duration
          ↓
    Saves data and logs
          ↓
    Commits updates back to GitHub

The collector currently runs Monday–Friday at:

- 7:30 AM
- 8:00 AM
- 8:30 AM
- 9:00 AM

## Project structure

    traffic-project/
    ├── .github/
    │   └── workflows/
    │       └── traffic.yml
    ├── data/
    │   └── traffic_data.csv
    ├── logs/
    │   └── traffic.log
    ├── traffic.py
    ├── .gitignore
    └── README.md

## Setup

Install dependencies:

    pip install requests python-dotenv

Create a `.env` file:

    GOOGLE_MAPS_API_KEY=your_api_key_here

Do not commit `.env` to GitHub.

For GitHub Actions, add the same key as a repository secret named:

    GOOGLE_MAPS_API_KEY

## Running locally

    python traffic.py

The script automatically skips weekends.

## Data and logs

Traffic measurements are stored in:

    data/traffic_data.csv

Logs are stored in:

    logs/traffic.log

## Future ideas

- Traffic trend analysis
- Best departure time recommendations
- Day-of-week comparisons
- Weather correlation
- Dashboard and visualisations