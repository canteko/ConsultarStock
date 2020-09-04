import telebot
from pyquery import PyQuery as pq
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

#Importamos la key del bot
bot=telebot.TeleBot("1310363512:AAEvI11_M_yuAEY3_Vg9VbpwCW0_5xi3UmU")

#Declaramos la ubicación y el tamaño de ventana de chrome
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

#Declaramos las opciones necesarias para que abra el navegador en segundo plano
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

#Abrimos el navegador
#driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver = webdriver.Chrome()  

#Bucle infinito
while(1):
    #Limpiamos cache y cookies, por si acaso estamos consultando todo el rato una página cacheada
    driver.get('chrome://settings/clearBrowserData')
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)

    #Entramos en la web y obtenemos el body
    driver.get('https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/')
    element = driver.find_element_by_css_selector("body")
    elementHTML = element.get_attribute('innerHTML')

    #Cargamos el body en el PyQuery
    plates = pq(elementHTML)

    #Buscamos si hay stock con PyQuery en el div correspondiente
    stock10kg = plates('.sizes__info[data-weigt="10.252"]').parent().find('.sizes__stock').find('.sizes__stock__info').html()
    stock5kg = plates('.sizes__info[data-weigt="5.082"]').parent().find('.sizes__stock').find('.sizes__stock__info').html()

    #Imprimimos el stock para que quede en terminal, aunque lo suyo es guardarlo en un log
    print("10Kg: " + stock10kg)
    print("5Kg: " + stock5kg)

    #Si el resultado no es "QUEDAN 0", mandamos mensaje al telegramo correspondiente
    if(stock10kg != "QUEDAN 0"):
        string_stock = "Discos de 10Kg disponibles, mensaje de stock: '" + stock10kg + "'"  + " " +  "https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/"
        bot.send_message(77771278, string_stock)
        bot.send_message(324294249, string_stock)
        bot.send_message(8268229, string_stock)

    if(stock5kg != "QUEDAN 0"):
        string_stock = "Discos de 5Kg disponibles, mensaje de stock: '" + stock5kg + "'" + " " +  "https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/"
        bot.send_message(8268229, string_stock)

    #Dormimos el bot 10 segunditos que no nos salga el server muy caro
    time.sleep(10)