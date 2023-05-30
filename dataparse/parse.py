import requests
import json
from bs4 import BeautifulSoup as BS
from pprint import pprint


def game_parser(number: int) -> list:
    number = 570
    url = f'https://steamcharts.com/app/{number}'
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    dota = soup.find('table', class_='common-table').find_all('tr')
    result = []
    for item in dota:
        data = item.text.split()
        if (data[0] == 'Last'):
            continue
        result.append((
            data[0],
            data[1],
            data[2],
            number,
        ))
    return result


if __name__ == '__main__':
    print(parse(570))
