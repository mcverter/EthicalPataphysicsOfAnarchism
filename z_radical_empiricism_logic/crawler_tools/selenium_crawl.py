from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from constants import (SITE_FRENCH_DDF_ETYMOLOGY,
                       SITE_FRENCH_DDF_TOKEN)

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds



def get_single_div_using_selenium(url, token):
    print('gettong url', url)
    try:
        driver.get(url)
        text = driver.find_element(By.CLASS_NAME, token).text
        print(text)
        # TO fix all these regex warlings PEP W605
        return re.sub('^\(\d+\)', '', text)
    except Exception as error1:
        print(f"First Selenium Exception {error1}, {type(error1)}")

        try:
            text = driver.find_element(By.CLASS_NAME, token).text
            print(text)
            return re.sub('^\(\d+\)', '', text)
        except Exception as error2:
            print(f"Second Selenium Exception {error2}, {type(error2)}")
            return None

def get_dictionaire_des_francophone_etymology(word):
    return get_single_div_using_selenium(SITE_FRENCH_DDF_ETYMOLOGY + word, SITE_FRENCH_DDF_TOKEN)
