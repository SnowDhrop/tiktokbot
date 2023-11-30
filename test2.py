from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Pour éviter les problèmes de connexion sur tiktok, autant chargé un profil chrome qui est déjà connecté au compte tiktok.
# Le problème c'est que Chrome verrouille certains fichiers lorsqu'il est ouvert, même les fichiers des autres utilisateurs
# Il faut donc fermer toutes les instances de chrome pour pouvoir lancer selenium avec un profil spécifique.
# Et tiktok n'aime pas les anciennes versions de chrome. Il les considère comme des bots et ça devient impossible de se connecter.

#----------------------CONFIGURATION-----------------------
# options = Options()
options = Options()

#Create random user-agent
ua = UserAgent()
user_agent = ua.random
# print(user_agent) 


chromedriver_path = "C:/Program Files (x86)/chromedriver.exe"
service = Service(chromedriver_path) #Specify path to chromedriver


profile_path = "C:/Users/natha/AppData/Local/Google/Chrome/User Data/Default"



# options.add_argument(f'--user-agent={user_agent}') #add the random user-agent to selenium
# options.binary_location = "C:/Program Files (x86)/Win_x64_1135105_chrome-win/chrome-win/chrome.exe" #specify path to the other version of chrome
options.add_argument("user-data-dir=C:/Users/natha/AppData/Local/Google/Chrome/User Data")
options.add_argument("--profile-directory=Profile 1")
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-cache")

# options.add_argument("--disable-extensions")
# options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)


#--------------------BOT--------------------
driver.get('https://www.tiktok.com')

print("------------OUVERTURE DE LA PAGE--------------")

#------------------------PAS NECESSAIRE------------
# loginLinks = driver.find_elements(By.CSS_SELECTOR, "#loginContainer div[role='link']")
# loginMailLink = loginLinks[1]
# loginMailLink.click()

# #Choose to connect with email
# time.sleep(random.randint(5, 15)) 
# driver.find_element(By.CSS_SELECTOR, "#loginContainer a[href='/login/phone-or-email/email']").click()


# time.sleep(random.randint(20,30)) 
# inputUsername = driver.find_element(By.CSS_SELECTOR, "#loginContainer input[name='username']")
# inputUsername.send_keys("sushilooversss")

# time.sleep(random.randint(5, 10)) 
# inputPassword = driver.find_element(By.CSS_SELECTOR, "#loginContainer input[type='password']")
# inputPassword.send_keys("")

# time.sleep(random.randint(5, 10)) 
# driver.find_element(By.CSS_SELECTOR, "#loginContainer button[type='submit']").click()
# print("---------------CONNEXION------------")

time.sleep(5000)
