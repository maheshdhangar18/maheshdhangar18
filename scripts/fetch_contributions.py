import json
import requests
from bs4 import BeautifulSoup

USERNAME = "maheshdhangar18"
url = f"https://github.com/users/{USERNAME}/contributions"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

days = []
for td in soup.find_all("td", class_="ContributionCalendar-day"):
    level = td.get("data-level", "0")
    date = td.get("data-date", "")
    if date:
        days.append({"date": date, "level": int(level)})

with open("data/contributions.json", "w") as f:
    json.dump(days, f)

print("Data fetched successfully!")
