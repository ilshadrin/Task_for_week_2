s='"Привет как дела"'
print('начальная строка', s)

if  s.startswith('"')==True and s.endswith('"')==True:
    s=s.strip('"')
    print('обрезанная строка', s)
    s=s.split()
    print(len(s), 'слова')