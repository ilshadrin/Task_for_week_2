



number={'один':'1','два':'2','три':'3','четыре':'4','пять':'5','шесть':'6','семь':'7','восемь':'8','девять':'9','десять':'10'}
operations={'плюс':'+','минус':'-','делить':'/','умножить':'*'}

user_input='сколько будет четыре делить на два'

#user_input='сколько будет четыре минус шесть'

#print(user_input.find('минус'))

user_list=user_input.split()
print('ввод юзера в списке ', user_list)


if user_input.find('плюс')>0:

    number_1=number[user_list[2]]
    number_2=number[user_list[4]]  
    print(number_1)                     
    print(number_2)
    sum=float(number_1)+float(number_2)
    print(sum)
    
elif user_input.find('минус')>0:
    number_1=number[user_list[2]]
    number_2=number[user_list[4]]  
    print(number_1)                     
    print(number_2)
    minus=float(number_1)-float(number_2)
    print(minus)
elif user_input.find('делить')>0:
    number_1=number[user_list[2]]
    number_2=number[user_list[5]]  
    print(number_1)                     
    print(number_2)
    delen=float(number_1)/float(number_2)
    print(delen)
elif user_input.find('умножить')>0:
    number_1=number[user_list[2]]
    number_2=number[user_list[5]]  
    print(number_1)                     
    print(number_2)
    umnogen=float(number_1)*float(number_2)
    print(umnogen)

#print(user_list.index('пять'))