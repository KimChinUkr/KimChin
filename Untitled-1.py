#a = "55"         #string
#b = 12              #integer
#c = 12.5           #float

#res = float(a) + b + c
#print(res)
#res2 = float(b) * c //
#print(res2)




#a = input("Введите число")
#n1 = int(a)
#n2 = int(a * 2)
#print(n1 + n2)


#num = 46
#num2 = "string"

#print(num)
#print(num2 * 5)


#chisl = 5
#bookv = "F"
#Slov = "Privet"
#chsl = 90.2

#CONST = "67"

#print(Slov)



#a = int(input("Введите число с 4 символами"))

#n1 = round(a // 1000 % 10)
#n2 = round(a // 100 % 10)
#n3 = round(a // 10 % 10)
#n4 = round(a % 10)

#print(n1," ",n2," ",n3," ",n4)



#imy = input("Имя")
#familiy = input("Фамилия")
#vozrast = input("Возраст")

#print(imy,familiy,vozrast)


#surnmae = input("Kak zovut druga")

#print("Моего друга зловут" + " ", surnmae)



#n = 136
#n1 = 7
#print(n // n1)

#n = input("Pervaya")
#n2 = input("Vtoraya")
#n3 = input("Tretya")

#res = float(n) + float(n2) + float(n3)
#res2 = float(n) - float(n2) - float(n3)
#res3 = float(n) % float(n2) % float(n3)
#res4 = float(n) * float(n2) * float(n3)
#res5 = float(n) // float(n2) // float(n3)
#print(res)
#print(res2)
#print(res3)
#print(res4)
#print(res5)



#n = 12
#n1 = 12.5
#n2 = "12.5"

#res = float(n) + n1 + float(n2)
#print(res)


#chislo = float(input("Введите первое число"))
#chislo2 = float(input("Введите второе число"))
#znak = input("Введите знак")

#if znak == "+":
 #   print(chislo + chislo2)
#elif znak == "-":
 #   print(chislo - chislo2)
#elif znak == "*":
 #   print(chislo * chislo2)
#elif znak == "/":
 #   print(chislo / chislo2)



#chislo = float(input("Введите число"))
#if chislo < 0:
#    print("Отрицательное число")
#elif chislo == 0:
#    print("Число ровняется 0")
#else:"Положительное число"


#znachenie = input("Введите что-то")
#if znachenie.isalpha():
 #   print("Введите число")
#elif znachenie.isdigit():
#    print("Вы ввели число")


#vozrast = int(input("Введи возраст,сукаа!")
#if vozrast > str(18):
 #   print("ВАМ МОЖНО БУХАТЬ")
#elif vozrast == str(18):
#    print("ДА БЛЯТЬ,СОВЕРШЕННОЛЕТИЕ СУКА")
#else:print("НЕЕЕЕТ,БУХАТЬ РАНО")


#a = int(input("Введите первое число"))
#b = int(input("Введите второе число"))
#c = (input("Введите знак"))

#if c == "+":
 #   print(a + b)
#elif c == "-":
 #   print(a - b)
#elif c == "*":
 #   print(a * b)
#else:print(a / b)


#pay = int(input("Введите убытки: "))
#profit = int(input("Введите прибыль: "))

#if pay > profit:
 #   res = pay - profit
  #  print("Ваши убитки составила: ", res)
#elif profit > pay:
 #   res = profit - pay
  #  print("Ваша прибыль составили: ", res)
#else:
 #   print("Нет ни прибыли, ни убытков")


       #             a = int(input("Введите превое число"))
        #           b = int(input("Введите второе число"))
         #    c = int(input("Введите третье число"))
#
 #                  if a + b + c > 0:
  #                  res = a + b + c
   #                  print(res / 3)
    #                elif a ! == b ! == c !:
     #print("Oshbbka")



#a = int(input("Pervaya"))
#b = int(input("Vtoraya"))

#c = True if ((a % 2 == 0) and (b % 2 ==0)) else False
#print(c)



#a = 2
#b = 5
#if a % 2 == 0:
#	print (a, " - четное число")
#else:
#	print (b, " - четное число")


#a = 14
#if a > 10 and a != 12 and a <= 15 or a == 18:
#	print ("True!")


#a = int(input("Chislo1"))
#b = int(input("Chislo2"))
#c = int(input("Chislo3"))

#lis = [a,b,c] # Изначально пустой список
#print(lis)

#korteh = (a,b,c)
#print(korteh)



#a = input("НАПИШИ СУКА ЧИСЛА ЧЕРЕЗ ЁБАННУЮ ЗАПИТУЮ")
#list = a.split(",")
#tuple = tuple(list)
#print('Spisoc: ', list)
#print('Korteh: ',tuple)

#a = [1,2,3,4,5,6]
#new = list(a)
#print(a," | ",new)


#lis = [[2, 5, 6], [5, 7, 1], [3, 6, 7, 34, 7, 0]]
##   for el in innerList:
  #      print(el)


#a = 100
#while a >= 1:
 # if a == 50 or a == 99:
  #  a -= 1
  #print("Vihod",a)
  #a -= 1


#lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
#min = lis[0]
#for i in lis:
#  if i < min:
 #   min = i

#print ("Минимальное число: ", min)
##print ("Список до удаления: ", lis)
#lis.remove(min)
#print ("Список после удаления: ", lis)
#if min < 0:
#  lis.append(min)
##else:
  #lis.insert(0,min)
  #print("Список с добавленным элементом: ", lis)


  #n = int(input("Количество рядов:"));
  #for i in range(n):
  #  for j in range(i):
  #    print('# ', end="")
  #  print('')

  # Создаем вывод элементов в обратной последовательности
  #for i in range(n, 0, -1):  # Перебираем элементы с конца
  #  for  j in range(i):  # Пишем каждый из рядов
   #   print('# ', end="")
    #print('')



#a = 1
#while a > 10:
  #print("Введите значение ")
 # a += 1

