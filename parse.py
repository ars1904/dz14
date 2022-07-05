import requests
from bs4 import BeautifulSoup
import pprint

def parse():
    domain = 'https://pythondigest.ru/'
    url = f'{domain}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = {}
    news_a = soup.find_all('a', class_='issue-item-title')
    for one_news_a in news_a:
        text = one_news_a.text
        href = one_news_a.get('href')
        # print(text, href)
        # шаг 2
        url = f'{href}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # получаем заголовки
        time_date = soup.find('time')
        if time_date is not None:
            txt = time_date.get_text()
        titles = soup.find('h1', class_="tm-article-snippet__title tm-article-snippet__title_h1")
        if titles is not None:
            tit = titles.get_text()

            # добавим в словарь
        result[text] ={'дата':txt,'заголовок': tit}

    return result