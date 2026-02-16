import requests
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_headlines(url):
    """
    Fetch all valid headlines from given URL
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    headline_tags = soup.find_all(["h1", "h2", "h3"])

    headlines = set()

    for tag in headline_tags:
        text = tag.get_text(strip=True)

        if text and len(text) > 25:
            headlines.add(text)

    print(f"Total headlines fetched: {len(headlines)}")

    return sorted(headlines)


def save_to_file(headlines, filename="news_headlines.txt"):
    """
    Save headlines to a text file with timestamp
    """

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Top News Headlines\n")
        file.write(f"Scraped on: {now}\n")
        file.write("=" * 60 + "\n\n")

        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print(f"Headlines successfully saved to {filename}")


def main():
    url = "https://www.bbc.com/news"

    print("🔎 Fetching headlines...\n")

    headlines = fetch_headlines(url)

    if headlines:
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")

        save_to_file(headlines)
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()
