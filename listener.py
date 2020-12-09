import telebot
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Importamos la key del bot
bot=telebot.TeleBot("1310363512:AAEvI11_M_yuAEY3_Vg9VbpwCW0_5xi3UmU")

#Abrimos el navegador
#driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver = webdriver.Chrome()  
keepTrying = True

#Bucle infinito
while(keepTrying):
    #Limpiamos cache y cookies, por si acaso estamos consultando todo el rato una página cacheada
    driver.get('chrome://settings/clearBrowserData')
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)

    #Entramos en la web y obtenemos el body
    driver.get('https://www.decathlon.es/es/p/kettlebell-pesa-rusa-8kg-domyos-cross-fitness-musculacion/_/R-p-152873')
    # driver.get('https://www.decathlon.es/es/p/rack-cross-training-musculacion-domyos-500-squat-traction/_/R-p-158534?mc=8380452')
    cookieElement = driver.find_element_by_id("didomi-notice-agree-button")
    cookieElement.click()
    element = driver.find_element_by_id("ctaButton")
    if(element.is_displayed() == True):
        bot.send_message(77771278, "Hay")
        # element.click()
        driver.execute_script("arguments[0].click();", element) 
        keepTrying = False

    time.sleep(10)
