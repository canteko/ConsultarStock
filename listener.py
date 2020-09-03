import telebot
from pyquery import PyQuery as pq
import time
users={}
bot=telebot.TeleBot("1310363512:AAEvI11_M_yuAEY3_Vg9VbpwCW0_5xi3UmU")

while(1):
    plates = pq(url='https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/')

    stock10kg = plates('.sizes__info:contains("10 KG")').parent().find('.sizes__stock').find('.sizes__stock__info').html()
    stock5kg = plates('.sizes__info:contains("5 KG")').parent().find('.sizes__stock').find('.sizes__stock__info').html()

    if(stock10kg != "QUEDAN 0"):
        string_stock = "Discos de 10Kg disponibles, mensaje de stock: '" + stock10kg + "'"  + " " +  "https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/"
        bot.send_message(77771278, string_stock)
        bot.send_message(324294249, string_stock)
        bot.send_message(8268229, string_stock)

    if(stock5kg != "QUEDAN 0"):
        string_stock = "Discos de 5Kg disponibles, mensaje de stock: '" + stock5kg + "'" + " " +  "https://www.decathlon.es/es/p/disco-de-fundicion-28-mm-musculacion-0-5-kg-a-20-kg-domyos-cross-fitness/_/R-p-7278?mc=1042303&c=NEGRO/"
        bot.send_message(8268229, string_stock)

    bot.send_message(77771278, "Correcto")

    time.sleep(10)