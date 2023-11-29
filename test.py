from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent) #Create random user-agent

chromedriver_path = "C:/Program Files (x86)/chromedriver.exe"
service = Service(chromedriver_path) #Specify path to chromedriver
# driver = webdriver.Chrome()

options.add_argument(f'--user-agent={user_agent}') #add the random user-agent to selenium
options.binary_location = "C:/Program Files (x86)/Win_x64_1135105_chrome-win/chrome-win/chrome.exe" #specify path to the other version of chrome

driver = webdriver.Chrome(service=service, options=options)




driver.get("https://www.tiktok.com") # Ouvrir la page web

time.sleep(random.randint(60, 300))

# test = driver.find_element(By.ID, "login-btn")

# driver.close() # Fermer l'onglet
# driver.quit() # Fermer le navigateur
