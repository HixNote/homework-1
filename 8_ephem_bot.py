"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet(bot, update):
    user_text = update.message.text
    if user_text.split()[1]=='Mercury':
        update.message.reply_text(ephem.constellation(ephem.Mercury(date.today())))
    elif user_text.split()[1]=='Venus':
        update.message.reply_text(ephem.constellation(ephem.Venus(date.today())))
    elif user_text.split()[1]=='Mars':
        update.message.reply_text(ephem.constellation(ephem.Mars(date.today())))
    elif user_text.split()[1]=='Jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter(date.today())))
    elif user_text.split()[1]=='Saturn':
        update.message.reply_text(ephem.constellation(ephem.Saturn(date.today())))
    elif user_text.split()[1]=='Uranus':
        update.message.reply_text(ephem.constellation(ephem.Uranus(date.today())))
    elif user_text.split()[1]=='Neptune':
        update.message.reply_text(ephem.constellation(ephem.Neptune(date.today())))
    elif user_text.split()[1]=='Pluto':
        update.message.reply_text(ephem.constellation(ephem.Pluto(date.today())))
    else:
        update.message.reply_text('Не знаю такую планету')
 

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
