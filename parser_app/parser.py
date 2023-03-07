import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://rezka.ag/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',

}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find('div', class_='b-content__inline_item')
    news_movie = []
    for item in items:
        news_movie.append(
            {
                'title_url': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_='b-content__inline_item-link').get_text(),
                'image': URL + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
            }
        )
        return news_movie


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        news_movie1 = []
        for page in range(0, 1):
            html = get_html(f'https://rezka.ag/', params=page)
            news_movie1.extend(get_data(html.text))
            return news_movie1
            # print(f'\n{news_movie1}')
    else:
        raise Exception('parser error.....')


# parser()
