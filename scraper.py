import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_bbc_headlines():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [h3.text for h3 in soup.find_all('h3')]
    return headlines

def fetch_cnn_headlines():
    url = 'https://www.cnn.com/world'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [span.text for span in soup.find_all('span', class_='cd__headline-text')]
    return headlines

def fetch_reuters_headlines():
    url = 'https://www.reuters.com/news/world'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = [h2.text for h2 in soup.find_all('h2', class_='story-title')]
    return headlines

def save_headlines_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['Source', 'Headline'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    bbc_headlines = fetch_bbc_headlines()
    cnn_headlines = fetch_cnn_headlines()
    reuters_headlines = fetch_reuters_headlines()

    all_headlines = []
    all_headlines.extend([('BBC', headline) for headline in bbc_headlines])
    all_headlines.extend([('CNN', headline) for headline in cnn_headlines])
    all_headlines.extend([('Reuters', headline) for headline in reuters_headlines])

    save_headlines_to_csv(all_headlines, 'headlines.csv')
