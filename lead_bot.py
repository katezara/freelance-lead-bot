import requests

ADZUNA_APP_ID = "d85b2c19"
ADZUNA_APP_KEY = "8bd1c366651360a9f648221d3ad821b2"

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
