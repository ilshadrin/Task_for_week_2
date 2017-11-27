# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
import logging


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Пожалуйста введи строку формата а(операция)b='
    print(text)
    update.message.reply_text(text)


def calculator(bot, update):
    user_input=update.message.text 
    print('user_input', user_input)
    print('user_input.endswith(''='')', user_input.endswith('='))


    if user_input.endswith('=')==True:                     #Проверяем, что в конце есть =
        user_input= user_input.strip('=')                  #удаляем =
        print('user_input.strip',user_input.strip('='))
        if user_input.find('+')>0:                          #проверяем, что + есть в строке    
            print('user_input.find(''+'')',user_input.find('+') ) 
            user_list=user_input.split('+')                  #делаем из строки список, элементы разделены +   
            print('user_list',user_list )

            sum=int(user_list[0])+int(user_list[1])    # считаем суммму 0го и 1го элемента списка
            print('sum', sum)
            update.message.reply_text(sum)

        elif user_input.find('-')>0:
            print('user_input.find(''-'')',user_input.find('-') ) 

            user_list=user_input.split('-')
            print('user_list',user_list )

            minus=int(user_list[0])-int(user_list[1])
            print('minus', minus)
            update.message.reply_text(minus)
        elif user_input.find('/')>0:
            print('user_input.find(''/'')', user_input.find('/') ) 

            user_list=user_input.split('/')
            print('user_list',user_list )

            try:
                delen=int(user_list[0])/int(user_list[1])
            
            except ZeroDivisionError:
                   update.message.reply_text('На ноль делить нельзя!')
                                           

            print('delen', delen)
            update.message.reply_text(delen)

        elif user_input.find('*')>0:
            print('user_input.find(''*'')', user_input.find('*') ) 

            user_list=user_input.split('*')
            print('user_list',user_list )

            umnogen=int(user_list[0])*int(user_list[1])
            print('umnogen', umnogen)
            update.message.reply_text(umnogen)
        else:
            print('Что это за операция?')
            update.message.reply_text('Что это за операция?')
    else:
        print('Поставь знак ''=''')
        update.message.reply_text('Поставь знак ''=''')



    

def main():
    updater = Updater("478411131:AAFn2nvMqaDicbbqE2Xsta_L4cQu1MY-zPM")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(CommandHandler("calculator",calculator))
    dp.add_handler(MessageHandler(Filters.text, calculator))

    
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()