import logging





from posixpath import split
from unittest import result

#Updater - это компонент отвечающий за коммуникацию с сервером 
 #Telegram - именно он получает/передает сообщения.

#Кроме работы с командами, telegram-бот может работать с текстом, картинками, аудио и видео. 
  #MessageHandler позволяет обрабатывать все эти типы сообщений:
  
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


#Конфигурационную информацию в отдельный файл settings.py в нем все настройки
#API_KEY = "КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather"
#PROXY_URL = ""
#PROXY_USERNAME = ""
#PROXY_PASSWORD = ""
import settings


#Будем записывать отчет о работе бота
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

#Бот вызовет функцию greet_user, когда пользователь напишет команду /start или
#нажмет кнопку Start при первом подключении к боту.        
def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")


#Напишем функцию talk_to_me, которая будет "отвечать" пользователю
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    #Ответим пользователю на его сообщение при помощи update.message.reply_text():
    update.message.reply_text(text)



#Функция main() будет содержать в себе основной код бота.
#Именно с ее помощью мы будем запускать бот.
def main():

    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    #mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    mybot = Updater(settings.API_KEY, use_context=True)

    #будем использовать диспетчер mybot.dispatcher для того, 
    # чтобы при наступлении события вызывалась наша функция:

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
 
    #Добавим новый обработчик событий в main()
    #При использовании MessageHandler укажем, что мы 
    #хотим реагировать только на текстовые сообщения - Filters.text

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    #Залогируем в файл информацию о старте бота

    logging.info("Бот стартовал")

    # Командуем боту начать ходить в Telegram за сообщениями

    mybot.start_polling()

    # Запускаем бота, он будет работать, пока мы его не остановим принудительно

    mybot.idle()
 
# В питоне есть общепринятый способ решить эту проблему. Если вам нужно вызвать 
# функцию не внутри другой функции, она заключается в специальный блок, который 
# исполняется только при прямом вызове файла python bot.py и не вызывается при
#  импорте, например from bot import PROXY. Вот как это выглядит:

if __name__ == "__main__":

    # Вызываем функцию main() - именно эта строчка запускает бота
    
    main()    

