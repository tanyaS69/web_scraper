import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = soup.find_all("h2")
    
    with open("All_headlines.txt", "w", encoding="utf-8") as file:
        
        for headline in headlines:
            text = headline.get_text().strip()
            
            if text: 
                print(text)
                file.write(text + "\n")
    
    print("\nHeadlines saved successfully in All_headlines.txt")

else:
    print("Failed to retrieve website")
