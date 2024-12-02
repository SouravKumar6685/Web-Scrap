from datetime import date
from django.utils.timezone import now
from myapp.models import *
import requests
from bs4 import BeautifulSoup

def scrape_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_='ipc-list-card--border-line')
    for item in news_items:
        # Safely extract the title
        title_tag = item.find('a', class_="ipc-link ipc-link--base sc-ed7ef9a2-3 eDjiRr")
        title = title_tag.text.strip() if title_tag else "No title"

        # Safely extract the description
        description_tag = item.find('div', class_="ipc-html-content-inner-div")
        description = description_tag.text.strip() if description_tag else "No description"

        # Safely extract the image (if it exists)
        image_tag = item.find('img', class_="ipc-image")
        image = image_tag['src'] if image_tag else "No image found"

        # Safely extract the external link (if it exists)
        external_link_tag = item.find('a', class_="ipc-link")
        external_link = "No external link" 
        if external_link_tag:
            external_link = external_link_tag['href']

       
        # Prepare the data for saving to the database
        news_data = {
            "title": title,
            "description": description,
            "images": image,
            "external_link": external_link,
        }

        # Create the news item in the database
        News.objects.create(**news_data)
