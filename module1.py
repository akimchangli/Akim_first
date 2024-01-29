#from math import*
#from tkinter import INSERT
#print("Tahad ülesannet lahendada?")
#answer=input("Sisetage oma vanus: ")
#try:
#    if answer.lower()== "jah":
#        a=float(input("sisetaage a"))
#        b=float(input("sisetaage b"))
#        c=float(input("sisetaage c"))
#    D=b**2-4*a*c
#    if D>0:
#        x1=round((-b+math.sqrt(D))/(2*a),2)
#        x2=round((-b-math.sqrt(D))/(2*a),2)
#        print("Võrandil on kaks X")
#    elif D==0:
#        x=round(-b/(2*a),2)
#        print("Võrandil on üks X")
#    else:
#        print("Võrandil on pole lahendeid")
#else:
#    print("Head aega!")

#vastus=input("Kas lahendame ruutvõrrand?").lower()
#if vastus=="jah":
#    print("Ruutvõrrandi lahendamine: ")
#    try:
#        a,b,c=map(float,input("a,b,c:")).splite()
#        #a=float(input("a: "))
#        #a=float(input("b: "))
#        #a=float(input("c: "))
#        D=b**2-4*a*c
#        if D>0:
#            x1=(-b+sqrt(D))/2*a
#            x2=(-b-sqrt(D))/2*a
#            print("2 lahendust 1:{x1:.2f}, 2:{x2:.2f}".format(x1,x2))
#        elif D==0:
#            x=(-b)/(2*a),2
#            print("1 lahendust: {0:.2f}".format(x1))
#        else:
#            print("Võrandil on pole lahendeid")
#    except :
#        print("Viga andmetüübiga")
#else:
#    print("Head aega!")

#import random

#number=random.randint(-200,500)
#if number>0:
#    print("Positiivne")
#elif number<0:
#    print("Negatiivne")
#else:
#    print("null")

#if number %2==0:
#    parity="Isegi"
#else:
#    parity="Mitte isegi"

#print(f"Genereeritud number","")

#a = float(input("Введите первое число: "))
#b = float(input("Введите второе число: "))
#c = float(input("Введите третье число: "))

#if a > 0 and b > 0 and c > 0:
    
#    if a + b > c and a + c > b and b + c > a:
        
#        angle_sum = a + b + c
        
#        if angle_sum == 180:
            
#            if a == b == c:
#                print("Треугольник равносторонний.")
#            elif a == b or b == c or a == c:
#                print("Треугольник равнобедренный.")
#            else:
#                print("Треугольник разносторонний.")
        
#        else:
#            print("Сумма углов не равна 180, поэтому это не треугольник.")
    
#    else:
#        print("Такие длины сторон не могут образовать треугольник.")
#else:
#    print("Введите положительные числа.")

#a,b,c=map(float,input("a,b,c:").split())
#if a>0 and b>0 and c>0:
#    if a+b+c==180:
#        print("Kolmurk")
#        if a==b==c:
#            print("võrkülgne")
#        elif a==b or b==c or a==c:
#            print("võrdhaarne")
#        else:
#            print("Сумма углов не равна 180, поэтому это не треугольник.")
#    else:
#        print("Nurgad")
#else:
#    print("<0")


#answer = input("Вы хотите расшифровать порядковый номер дня недели в название? (да/нет): ")
#if answer.lower() == "да":
#    number = int(input("Введите число от 1 до 7: "))
    
#    if number >= 1 and number <= 7:
#        import calendar
        
#        day_name = calendar.day_name[number - 1]
       
#        print(f"День недели под номером {number} - это {day_name}.")
#    else:
#        print("Ошибка: введите число от 1 до 7.")
#else:
#    print("До свидания!")

#14 korrutustabel
#
#for j in range(1,11):
#    for i in range(1, 11):
#        print("{:4}".format (j*i), end=" ")
#    print()




#12 pank
#from datetime import*
#from random import*

#algsumma = float(input("Какую сумму вы желаете вложить?"))
#alg = lõppsumma = algsumma
#intress = randint(1,10)
#print(f"Платеж в банк  на сумму {algsumma}. С процентной ставкой {intress}")
#aastad = int(input("На какой срок желаете сделать вклад?"))
#print("Aasta Algsumma Intress Aasta_lõpuks")
#for i in range(1, aastad+1):
#    print(i)
#    intsumma = algsumma * (intress / 100)
#    lõppsumma = algsumma+intsumma
#    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
#    algsumma=lõppsumma
#print(f"Summa kokku: {lõppsumma} Eur")
#print(f"Kasum: {lõppsumma-alg} Eur")

#import turtle
#def draw_grid(vertical, horizontal):
#    for _ in range(vertical):
#        for _ in range(horizontal):
#            for _ in range(4):
#                turtle.forward(50)
#                turtle.right(90)
#            turtle.forward(50)
#        turtle.backward(50 * horizontal)
#        turtle.right(90)
#        turtle.forward(50)
#        turtle.left(90)

#    turtle.done()

#vertical_sqr = int(input("Введите количество вертикальных квадратов: "))
#horizontal_sqr = int(input("Введите количество горизонтальных квадратов: "))

#draw_grid(vertical_sqr, horizontal_sqr)

from abc import ABC
print("* ИГРЫ С ЧИСЛАМИ *")
print()
while 1:
    try:
        a = int(input("Введите целое число => "))
        break
    except ValueError:
         print("Это не целое число")
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    b=a
    paaris = 0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Перевёрнутое* число", b)
    print()
    print("Проверяем гипотезу Сиракуз")
    print()
    c=b
    if c % 2 == 0:
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
            if c % 2 == 0:
                    c = c // 2
            else:
                    c = (3*c + 1) //+ 2
            print(c, end=" ")
    print()
    print("Гипотенуза верна")
