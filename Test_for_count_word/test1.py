


s='"Привет как дела"'
s='            '

#s=input('input')
print('начальная строка', s)

'''
a="     "
print('a ', a)

b=a.strip(' ')

print('длина а без пробелов', len(b))
#print('len a ', len(a))

'''



print('start', s.startswith('"')) #проверяем на кавычки в конце
print('end', s.endswith('"'))    #проверяем на кавычки в начале
print('Строка без кавычек ', s.strip('"')) #удаляем кавычки

s=s.split() #Превращение строки в список
print('длина списка s ', len(s))

if len(s)!=0:
    print(s)
    print(len(s), 'слова')
else:
    print('Нулевая строка!')
    print('s', )