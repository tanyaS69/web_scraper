# web_scraper

## Project Overview
This project is a Python-based web scraper that automatically collects top news headlines from a public news website (BBC News) and saves them into a `.txt` file.

The project demonstrates basic to intermediate-level web scraping using:
* `requests` – to fetch HTML content
* `BeautifulSoup` – to parse and extract headline tags
* `datetime` – to add timestamp to output file


## Project Files
websc/
│
├── scrapper.py
├── scraps.py
├── news.py
│
├── headlines.txt
├── All_headlines.txt
├── new_headlines.txt
│
├── output/
│   ├── scrapper_out1.png & scrapper_out2.png
│   ├── scraps_output.png 
│   └── news_out1.png & news_out2.png
│
└── README.md



## Code Versions Included

### 1️) Basic Version[scrapper.py]
* Fetches website HTML
* Extracts `<h2>` headline tags
* Saves headlines into `headlines.txt`
* Simple and beginner-friendly


### 2️) Intermediate Version[scraps.py]
* Adds User-Agent headers
* Includes proper error handling
* Removes duplicate headlines
* Adds timestamp to output file
* Uses modular functions for clean structure


### 3️) Advanced Version (No Limit)[news.py]
* Fetches all valid headlines
* Extracts `<h1>`, `<h2>`, and `<h3>` tags
* Uses `set()` for automatic duplicate removal
* Sorts headlines
* Displays total headlines fetched
* Professional formatting in output file


## Installation
Install required libraries:
pip install requests beautifulsoup4

## How to Run
python filename.py

After execution, `headlines.txt` files with different file names will be generated automatically for each versions.

## Learning Outcomes
* Automating data collection from a public website
* Understanding HTML parsing
* Handling HTTP requests and errors
* Writing clean, modular Python code
* Saving scraped data to external files

## Future Improvements
* Scrape multiple news websites
* Save data in CSV/JSON format
* Add logging system
* Convert into a scheduled automation task

