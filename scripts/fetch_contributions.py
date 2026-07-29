import os
import json
import requests
from bs4 import BeautifulSoup

def fetch_data():
    user = os.environ.get("GITHUB_USER", "torvalds") # fallback for local testing
    url = f"https://github.com/users/{user}/contributions"
    print(f"Fetching contributions for {user}...")
    
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    
    days = []
    for td in soup.find_all("td", class_="ContributionCalendar-day"):
        date = td.get("data-date")
        level = td.get("data-level", 0)
        if date:
            days.append({"date": date, "level": int(level)})
            
    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w") as f:
        json.dump({"days": days}, f, indent=2)
    print("Saved to data/contributions.json")

if __name__ == "__main__":
    fetch_data()
