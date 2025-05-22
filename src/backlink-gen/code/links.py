import json
import requests
import sys
from urllib.parse import urlparse

def load_backlink_data():
    """
    Read and load the backlink.json file
    """
    try:
        with open("code/backlink.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] backlink.json file not found.")
        sys.exit()
    except json.JSONDecodeError:
        print("[!] Failed to parse backlink.json file.")
        sys.exit()

def check_backlink(site, backlink_data):
    """
    Check the status of each backlink
    """
    for backlink in backlink_data:
        url = backlink['url'].replace("uhaka.com", site)
        try:
            response = requests.get(url)
            status_code = response.status_code
        except KeyboardInterrupt:
            sys.exit()
        except:
            status_code = "Request failed"

        domain = urlparse(url).netloc  # Use urlparse to extract the domain part
        print(f"~ {site} | Result -> {domain} Status: {status_code}")

        if status_code == 200 or status_code == 502:
            with open("200status.txt", "a+") as file:
                file.write(url + "\n")

def main():
    """
    Main function, connects various sub-functions
    """
    domain = "www.uhaka.com"  # Modify this variable to control the site to add backlinks to
    backlink_data = load_backlink_data()
    check_backlink(domain, backlink_data)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n\n -> Exited due to error: {e}\n")