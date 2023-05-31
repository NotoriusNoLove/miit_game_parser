import requests
import json
from bs4 import BeautifulSoup as BS
from pprint import pprint
import datetime


def game_parser(number: int) -> list:
    # number = 570
    url = f'https://steamcharts.com/app/{number}'
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    dota = soup.find('table', class_='common-table').find_all('tr')
    result = []
    for item in dota:
        data = item.text.split()
        if (data[0] == 'Last' or data[0] == 'Month'):
            continue
        result.append((
            datetime.datetime.strptime(data[0][0:3] + " " + data[1], '%b %Y'),
            data[2],
            number,
        ))
    return result
