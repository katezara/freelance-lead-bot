import requests
import time
import os

# Airtable credentials
AIRTABLE_TOKEN = os.environ["AIRTABLE_TOKEN"]
BASE_ID = os.environ["BASE_ID"]
TABLE_NAME = "Job Leads"

AIRTABLE_TOKEN = "patABC123XYZ456"
BASE_ID = "appXJDF8392JDK"
TABLE_NAME = "Job Leads"
import requests
import time

# Adzuna API credentials
APP_ID = "d85b2c19"
APP_KEY = "8bd1c366651360a9f648221d3ad821b2"

# Search terms
search_terms = [
    "wordpress developer",
    "web designer",
    "website redesign",
    "ui ux designer",
    "figma designer",
    "shopify developer",
    "webflow designer",
    "landing page designer"
]

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"

for term in search_terms:

    print(f"\n🔎 Searching for: {term}\n")

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": term,
        "results_per_page": 10,
        "content-type": "application/json"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("API Error:", response.text)
        continue

    data = response.json()

    jobs = data.get("results", [])

    if not jobs:
        print("No jobs found")
        continue

    for job in jobs:

        title = job.get("title")
        company = job.get("company", {}).get("display_name")
        location = job.get("location", {}).get("display_name")
        url = job.get("redirect_url")

        print("💼 Job:", title)
        print("🏢 Company:", company)
        print("📍 Location:", location)
        print("🔗 Link:", url)
        print("-" * 50)

    # Avoid hitting API limits
    time.sleep(2)
