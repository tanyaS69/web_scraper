import requests
from bs4 import BeautifulSoup

# Step 1: Website URL (Example: BBC News)
url = "https://www.bbc.com/news"

# Step 2: Send request to fetch HTML content
response = requests.get(url)

# Step 3: Check if request was successful
if response.status_code == 200:
    
    # Step 4: Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 5: Find all headline tags (BBC uses h2 for headlines)
    headlines = soup.find_all("h2")
    
    # Step 6: Open a text file to save headlines
    with open("All_headlines.txt", "w", encoding="utf-8") as file:
        
        for headline in headlines:
            text = headline.get_text().strip()
            
            if text:  # Avoid empty titles
                print(text)
                file.write(text + "\n")
    
    print("\nHeadlines saved successfully in All_headlines.txt")

else:
    print("Failed to retrieve website")
