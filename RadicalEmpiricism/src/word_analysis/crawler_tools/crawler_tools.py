import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from RadicalEmpiricism.src.constants import (SITE_FRENCH_DDF_ETYMOLOGY,
                                             SITE_FRENCH_DDF_TOKEN,
                                             SITE_FRENCH_CNRTL_ETYMOLOGY)

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds


def get_soup_from_url(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def get_single_div_using_bs4(url, token):
    soup = get_soup_from_url(url)
    # results = soup.find_all('div')
    return soup.find('div', {"class": token})


def get_single_div_using_selenium(url, token):
    print('gettong url', url)
    try:
        driver.get(url)
        text = driver.find_element(By.CLASS_NAME, token).text
        print(text)
        return re.sub('^\(\d+\)', '', text)
    except Exception as err:
        print(f"First Selenium Exception {err=}, {type(err)=}")

        try:
            text = driver.find_element(By.CLASS_NAME, token).text
            print(text)
            return re.sub('^\(\d+\)', '', text)
        except Exception as err:
            print(f"Second Selenium Exception {err=}, {type(err)=}")
            return None


def get_dictionaire_des_francophone_etymology(word):
    return get_single_div_using_selenium(SITE_FRENCH_DDF_ETYMOLOGY + word, SITE_FRENCH_DDF_TOKEN)


def get_cntrl_eymology(word):
    page = requests.get(SITE_FRENCH_CNRTL_ETYMOLOGY + word)
    text = page.text
    start = text.find('Étymol. et Hist.')
    end = text.find('</div', start)
    div = text[start:end]
    div = re.sub('<.*?>', '', div)
    div = re.sub('\s+$', '', div)
    print('div', div)
    return div