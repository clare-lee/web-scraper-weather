import requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=40.7678&lon=-73.9645"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Get current conditions
current_f = soup.find("p", class_="myforecast-current-lrg")
current_c = soup.find("p", class_="myforecast-current-sm")
current_condition = soup.find("p", class_="myforecast-current")

print(
    "Current Weather:",
    current_f.get_text(),
    "/",
    current_c.get_text(),
    current_condition.get_text(),
)
