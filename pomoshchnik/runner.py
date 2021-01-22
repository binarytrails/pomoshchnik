# @author Vsevolod Ivanov <seva@binarytrails.net>

import time
import traceback
from selenium import webdriver

from pomoshchnik import cli
from pomoshchnik import loader

def interactive(page='https://google.com'):
    print(cli.__banner__)
    ff = loader.firefox(anon=True)
    if (page):
        loader.load(ff, 'https://google.com', timeout=5)
    return ff

def loop():
    while True:
        try:
            print('hello from loop')
            time.sleep(1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(traceback.print_exc())
