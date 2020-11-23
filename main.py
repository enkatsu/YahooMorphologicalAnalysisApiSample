import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET

URL = 'https://jlp.yahooapis.jp/MAService/V1/parse'

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get('CLIENT_ID')


def request_yahoo_api(text: str) -> ET.Element:
    """
    Yahoo!の形態素解析APIを使用する関数
    .envのDEBUGが空なら実際にHTTPリクエストを行う。
    空以外ならHTTPリクエストは行わず、ローカルのファイルを開いく。
    :param text:
    :return:
    """
    is_debug = os.environ.get('DEBUG')
    print('is_debug: %s' % bool(is_debug))
    if is_debug:
        return ET.parse('xml/sample.xml').getroot()
    results = 'ma'
    response = requests.get(f'{URL}?appid={CLIENT_ID}&sentence={text}&results={results}')
    if response.status_code != 200:
        response.raise_for_status()
    return ET.fromstring(response.text)


def main():
    text = 'こんにちは。今日も寒いですね。'
    tree = request_yahoo_api(text)
    for word in tree.findall('.//{*}word'):
        surface = word.find('.//{*}surface')
        reading = word.find('.//{*}reading')
        pos = word.find('.//{*}pos')
        print(surface.text, reading.text, pos.text)


if __name__ == '__main__':
    main()
