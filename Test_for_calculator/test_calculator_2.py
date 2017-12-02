



user_input='50/2='

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

    elif user_input.find('-')>0:
        print('user_input.find(''-'')',user_input.find('-') ) 

        user_list=user_input.split('-')
        print('user_list',user_list )

        minus=int(user_list[0])-int(user_list[1])
        print('minus', minus)
    elif user_input.find('/')>0:
        print('user_input.find(''/'')', user_input.find('/') ) 

        user_list=user_input.split('/')
        print('user_list',user_list )

        delen=int(user_list[0])/int(user_list[1])
        print('delen', delen)
    else:
        print('Что это за операция?')
else:
    print('Поставь знак ''=''')
