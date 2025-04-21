import requests
from bs4 import BeautifulSoup

def scrape_wiki(url: str , file_name : str):

    # Send a GET request to the webpage
    response = requests.get(url)

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all the text from the page
    paragraph = soup.find_all('p')

    # Optionally, save the scraped content to a text file
    with open(f'../data_file/{file_name}.txt', mode= 'w', encoding='utf-8') as file:
        for para in paragraph:
            file.write(para.get_text())


url="https://en.wikipedia.org/wiki/97th_Academy_Awards"
scrape_wiki(url,'oscars2025')

