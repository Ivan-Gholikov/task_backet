# Даны 2 ведра, первое ведро - 5 л, второе ведро - 3л . и не ограниченное количество воды. 
# Нужно отмерить 4 л, в другие емкости переливать нельзя.

# Создадим 2 переменные 
bucket_one = 5
bucket_two = 3

#Возьмем первое ведро, и отмерим половину у него, получим 2,5 л
resto = bucket_one / 2

#Возьмем второе ведро, и отмерим половину у него , получаем 1,5 л
yumm = bucket_two / 2

#Затем из второго ведра перельем в первое ведро, получаем наши 4 л

tupp = yumm + resto
print(int(tupp))

#Запишим данную задачу в виде выражения
tumm = (bucket_one / 2) + (bucket_two / 2)
print(int(tumm))