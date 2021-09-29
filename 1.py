name = input('Введите имя студента: ')
secondname = input('Введите фамилию студента: ')
yearofbirthday = int(input('Введите год рождения студента: '))
print(name, secondname, yearofbirthday, sep = "_")
name, secondname = secondname, name
print(name, secondname, yearofbirthday+60, sep = "_" )
