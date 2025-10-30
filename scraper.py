import requests
from bs4 import BeautifulSoup

URL = "https://forecast.weather.gov/MapClick.php?lat=40.7678&lon=-73.9645"

try:
    page = requests.get(URL)
    page.raise_for_status()

    soup = BeautifulSoup(page.content, "html.parser")

    # ANSI escape codes
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # print location in single line
    # text = location.get_text().replace("Lon:", " Lon:").replace("Elev:", " Elev:")
    # print("Location:", text.strip())

    location = soup.find("span", class_="smallTxt")

    if location:
        print(f"{BOLD}Location:{RESET}")
        for index, item in enumerate(location, start=1):
            text = item.text.strip()
            if text:
                print(f" {text}", end=" ")
                if index % 2 == 0:
                    print()
    print()

    # Get current conditions
    current_f = soup.find("p", class_="myforecast-current-lrg")
    current_c = soup.find("p", class_="myforecast-current-sm")
    current_condition = soup.find("p", class_="myforecast-current")

    print(f"{BOLD}Current Weather:{RESET}")
    print(f"  Temperature: {current_f.get_text()} / {current_c.get_text()}")
    print(f"  Conditions: {current_condition.get_text()}")

except requests.Timeout:
    print("Request timed out")
except requests.ConnectionError:
    print("Could not connect to weather.gov")
except requests.RequestException as e:
    print(f"Network error: {e}")
