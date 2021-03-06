'''
Научите бота выполнять основные арифметические действия с числами: сложение, вычитание, умножение и деление. Если боту сказать “2-3=”, он должен ответить “-1”. Все выражения для калькулятора должны заканчиваться знаком равно.

Дополнительно: не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль.

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

            try:
                sum=int(user_list[0])+int(user_list[1])    # считаем суммму 0го и 1го элемента списка
            except ValueError:
                   update.message.reply_text('Это не число!')

            print('sum', sum)
            update.message.reply_text(sum)

        elif user_input.find('-')>0:
            print('user_input.find(''-'')',user_input.find('-') ) 

            user_list=user_input.split('-')
            print('user_list',user_list )

            try:
                minus=int(user_list[0])-int(user_list[1])
            except ValueError:
                   update.message.reply_text('Это не число!')

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
            except ValueError:
                   update.message.reply_text('Это не число!')                              

            print('delen', delen)
            update.message.reply_text(delen)

        elif user_input.find('*')>0:
            print('user_input.find(''*'')', user_input.find('*') ) 

            user_list=user_input.split('*')
            print('user_list',user_list )

            try:
                umnogen=int(user_list[0])*int(user_list[1])
            except ValueError:
                   update.message.reply_text('Это не число!')
                       
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
    dp.add_handler(MessageHandler(Filters.text, calculator))

    
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()