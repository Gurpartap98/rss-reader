import requests
import xml.etree.ElementTree as ET


def fetch_rss(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch RSS feed.")
        return

    root = ET.fromstring(response.text)

    print("\nLatest Articles:\n")

    for i, item in enumerate(root.findall(".//item")):
        if i >= 5:
            break

        title = item.find("title")
        link = item.find("link")
        description = item.find("description")

        print("----------")
        print("Title:", title.text if title is not None else "No title")
        print("Link:", link.text if link is not None else "No link")
        print("Description:", description.text if description is not None else "No description")


if __name__ == "__main__":
    print("RSS Reader Starting...")
    url = input("Enter RSS feed URL: ")
    fetch_rss(url)
