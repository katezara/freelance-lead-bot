import requests

ADZUNA_APP_ID = "YOUR_ID"
ADZUNA_APP_KEY = "YOUR_KEY"

url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

params = {
    "app_id": ADZUNA_APP_ID,
    "app_key": ADZUNA_APP_KEY,
    "what": "wordpress developer",
    "results_per_page": 5
}

response = requests.get(url, params=params)
jobs = response.json()["results"]

for job in jobs:
    print(job["title"], job["redirect_url"])
