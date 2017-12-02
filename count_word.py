'''

Добавить команду /wordcount котрая считает сова в присланной фразе. Например на запрос /wordcount "Привет как дела" бот должен посчитать количество слов в кавычках и ответить: 3 слова.

Не забудьте: добавить проверки на наличие кавычек, пустую строку. 

'''

# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
import logging


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start. Я есть'
    #print(1/0)
    print(text)
    update.message.reply_text(text)


def wordcount(bot, update):
    word_user=update.message.text
    print('начальная фраза ', word_user)
    word_user=word_user[11:]
    print('обрезанная фраза', word_user)

   

    if  word_user.startswith('"')==True and word_user.endswith('"')==True: #проверяем на кавычки в начале и конце
            word_user=word_user.strip('"')           #удаляем кавычки
            print('обрезанная строка', word_user)
            word_user=word_user.split()                   #Превращение строки в список
            print('список word_user', word_user) 
            if len(word_user)!=0:                   #если длина списка не равна нулю
                print(len(word_user), 'слова')
                update.message.reply_text('{} {}'.format(len(word_user), 'слова'))   #вывод количества слов в списке, т.е. введнных пользователем
            else :
                update.message.reply_text('Пустая строка!')
    else :
        update.message.reply_text('Не хватает кавычек!')

def main():
    updater = Updater("478411131:AAFn2nvMqaDicbbqE2Xsta_L4cQu1MY-zPM")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount",wordcount))

    
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
