import re

import requests
from bs4 import BeautifulSoup
from constants import  SITE_FRENCH_CNRTL_ETYMOLOGY



def get_soup_from_url(url):
    page = requests.get(url, timeout=10)
    return BeautifulSoup(page.content, "html.parser")


def get_single_div_using_bs4(url, token):
    soup = get_soup_from_url(url)
    # results = soup.find_all('div')
    return soup.find('div', {"class": token})


def get_cntrl_eymology(word):
    page = requests.get(SITE_FRENCH_CNRTL_ETYMOLOGY + word, timeout=10)
    text = page.text
    start = text.find('Étymol. et Hist.')
    end = text.find('</div', start)
    div = text[start:end]
    div = re.sub('<.*?>', '', div)
    div = re.sub('\s+$', '', div)
    print('div', div)
    return div
