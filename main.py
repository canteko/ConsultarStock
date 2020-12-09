import telebot
from pyquery import PyQuery as pq
users={}
bot=telebot.TeleBot("1310363512:AAEvI11_M_yuAEY3_Vg9VbpwCW0_5xi3UmU")

def listener(messages):
    for m in messages:
        plid=m.chat.id
        print(plid)
        if m.content_type=="text":
            if not m.text[0]=='/' and str(plid) not in users:
            	bot.send_message(plid, "To begin, type '/start'") 

bot.set_update_listener(listener)


bot.polling()           
