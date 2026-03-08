import requests
import time
import os

import os

AIRTABLE_TOKEN = os.environ["AIRTABLE_TOKEN"]
BASE_ID = os.environ["BASE_ID"]

# ==========================
# ADZUNA API CONFIG
# ==========================

ADZUNA_APP_ID = "d85b2c19"
ADZUNA_APP_KEY = "8bd1c366651360a9f648221d3ad821b2"

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/1"


# ==========================
# SEARCH KEYWORDS
# ==========================

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


# ==========================
# AIRTABLE CONFIG
# ==========================

AIRTABLE_TOKEN = os.environ["AIRTABLE_TOKEN"]
BASE_ID = os.environ["BASE_ID"]
TABLE_NAME = "Job Leads"


# ==========================
# SEND RECORD TO AIRTABLE
# ==========================

def send_to_airtable(title, company, location, link, keyword):

    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "Title": title,
            "Company": company,
            "Location": location,
            "Keyword": keyword,
            "Link": link,
            "Source": "Adzuna",
            "Status": "New"
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print("❌ Airtable error:", response.text)
    else:
        print("✅ Lead added to Airtable")


# ==========================
# SEARCH JOBS IN ADZUNA
# ==========================

def search_jobs(term):

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": term,
        "results_per_page": 10
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("❌ API error:", response.text)
        return

    data = response.json()

    jobs = data.get("results", [])

    if not jobs:
        print("No jobs found for:", term)
        return

    for job in jobs:

        title = job.get("title")
        company = job.get("company", {}).get("display_name")
        location = job.get("location", {}).get("display_name")
        link = job.get("redirect_url")

        print("\n💼 Job:", title)
        print("🏢 Company:", company)
        print("📍 Location:", location)
        print("🔗 Link:", link)

        send_to_airtable(title, company, location, link, term)

        print("-" * 40)

def send_telegram_message(message):

    url = f"https://api.telegram.org/bot{8561841506:AAFMtPORf1nHYVElQXGuxtsA6_NL60-_hRM}/sendMessage"

    payload = {
        "chat_id": 7782399136,
        "text": message,
        "parse_mode": "Markdown"
    }

    requests.post(url, json=payload)


# ==========================
# MAIN BOT RUNNER
# ==========================

def run():

    print("\n🚀 Freelance Lead Bot Started\n")

    for term in search_terms:

        print(f"\n🔎 Searching for: {term}")

        search_jobs(term)

        # avoid hitting API rate limits
        time.sleep(2)


if __name__ == "__main__":
    run()
