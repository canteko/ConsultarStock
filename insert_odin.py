import telebot
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

#Abrimos el navegador
driver = webdriver.Chrome(ChromeDriverManager().install())

#Entramos en la web y obtenemos el body
driver.get('https://www.eurotransportcar.com/es')

with open('load_odin.js', 'r') as file:
    script = file.read().replace('\n', '')

print(script)

time.sleep(1)
driver.execute_script(script)
print("Executed")
time.sleep(5)