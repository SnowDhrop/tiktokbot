# J'EXPLORE ET TEST LA PLUPART DES FONCTIONNALITES DE SELENIUM, CE QUI EN FAIT UNE BONNE DOC


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

#----------------------CONFIGURATION-----------------------
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



#----------------------------BOT----------------------
driver.get("https://www.tiktok.com") # Ouvrir la page web

# WebDriverWait(driver, random.randint(30, 50)).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app"))) #Attend que l'élément soit chargé
time.sleep(random.randint(30,60))
first_button = driver.execute_script("""
    return document.querySelector('tiktok-cookie-banner').shadowRoot.querySelector('button');
""") #Sélectionne le bouton "refuser les cookies" avec js
first_button.click() #Clique sur le bouton "refuser les cookies"
print("-------------REFUSER LES COOKIES OK-----------")


# time.sleep(random.randint(10, 30))
WebDriverWait(driver, random.randint(10, 30)).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-login-button"))) #Attend que l'élément soit chargé
loginButton = driver.find_element(By.CSS_SELECTOR, "#header-login-button") #selectionne bouton login
loginButton.click()
print("---------------LOGIN BUTTON OK-------------")

while True:  #Tant que le lien pou rentrer ses identifiants n'est pas visible, tu rafraichis la page et tu cliques sur le bouton login, avec des delays aléatoires
    try:
        WebDriverWait(driver, random.randint(30, 60)).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginContainer div[role='link']")))
        break

    except TimeoutException:
        print("-----------REFRESH PAGE----------")
        driver.refresh()   
        time.sleep(random.randint(10, 30))

        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-login-button"))) #Attend que l'élément soit chargé
        loginButton = driver.find_element(By.CSS_SELECTOR, "#header-login-button") #selectionne bouton login
        loginButton.click()
        time.sleep(random.randint(5, 10))
        

print("----------------LIENS DE CONNEXION OK----------------")

time.sleep(random.randint(10, 20))        
loginLinks = driver.find_elements(By.CSS_SELECTOR, "#loginContainer div[role='link']")
loginMailLink = loginLinks[1]
loginMailLink.click()

#Choose to connect with email
time.sleep(random.randint(5, 15)) 
driver.find_element(By.CSS_SELECTOR, "#loginContainer a[href='/login/phone-or-email/email']").click()


time.sleep(random.randint(5, 15)) 
inputUsername = driver.find_element(By.CSS_SELECTOR, "#loginContainer input[name='username']")
inputUsername.send_keys("sushilooversss")

time.sleep(random.randint(5, 10)) 
inputPassword = driver.find_element(By.CSS_SELECTOR, "#loginContainer input[type='password']")
inputPassword.send_keys("Pyromanciens1357!")

time.sleep(random.randint(5, 10)) 
driver.find_element(By.CSS_SELECTOR, "#loginContainer button[type='submit']").click()
print("---------------CONNEXION------------")


time.sleep(5000)

# test = driver.find_element(By.ID, "login-btn")

# driver.close() # Fermer l'onglet
# driver.quit() # Fermer le navigateur
