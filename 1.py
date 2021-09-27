name = input('Введите имя студента: ')
secondname = input('Введите фамилию студента: ')
yearofbirthday = int(input('Введите год рождения студента: '))
name, secondname = secondname, name
print(name, secondname, yearofbirthday, sep = "_")
print(name, secondname, yearofbirthday+60, sep = "_" )
