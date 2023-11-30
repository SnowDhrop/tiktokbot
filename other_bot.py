import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


print('=====================================================================================================')
print('Heyy, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
print('=====================================================================================================')
# time.sleep(8)
print('Running bot now, get ready and login manually...')
# time.sleep(4)

options = webdriver.ChromeOptions()
chromedriver_path = "C:/Program Files (x86)/chromedriver.exe"
service = Service(chromedriver_path) #Specify path to chromedriver


bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options )
bot.set_window_size(1680, 900)

bot.get('https://www.tiktok.com/login')
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
ActionChains(bot).key_down(Keys.CONTROL).send_keys(
    '-').key_up(Keys.CONTROL).perform()
print('Waiting 50s for manual login...')
time.sleep(5000)
# bot.get('https://www.tiktok.com/upload/?lang=en')
# time.sleep(3)