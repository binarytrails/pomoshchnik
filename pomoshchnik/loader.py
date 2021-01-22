# @author Vsevolod Ivanov <seva@binarytrails.net>

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def firefox(binary='/usr/bin/firefox', marionette=True, anon=True):
    capabilities = webdriver.DesiredCapabilities.FIREFOX
    capabilities['marionette'] = marionette
    capabilities['binary'] = binary
    options = webdriver.FirefoxOptions()
    if (anon):
        options.add_argument('--private-window')
    return webdriver.Firefox(capabilities=capabilities, options=options)

def load(driver, url, timeout=3):
    timeout = 3
    try:
        driver.get(url)
        main_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(main_present)
    except TimeoutException:
        print("! page loading timeout ")
    finally:
        print("+ page loaded")
