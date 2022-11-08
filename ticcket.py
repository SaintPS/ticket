ticket = int(input("Введите количество билетов: "))         #Пользователь вводит количество билетов
people_age = []
for i in range(ticket):
    print(("Введите возраст участника №"),i + 1)
    age = int(input(""))                                    #Пользователь указывает возраст участников согласно билетов
    people_age.append(age)                                  #Возраст участников добавляется в общий список

Group1 = len([item for item in people_age if item < 18])                    # Переменная для подсчета участников младше 18
Group2 = len([item for item in people_age if (item >= 18 and item < 25)])   # Переменная для подсчета участников старше 18 и мл. 25
Group3 = len([item for item in people_age if item >= 25])                   # Переменная для подсчета участников старше 25
GroupALL = Group1 + Group2 + Group3                                         # Переменная для подсчета всех участников

if GroupALL > 3:
    print ("Сумма к оплате со скидкой", (Group2 * 990+Group3 * 1390) - (Group2 * 990+Group3 * 1390)*0.1)
else:
    print ("Сумма к оплате", Group2 * 990 + Group3 * 1390)



