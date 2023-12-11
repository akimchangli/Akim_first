
from math import*
import math


#kokku=randint(1,100)
#print("Laual peal on",kokku,"kommid. Mitu tahad süüa?")
#kommid=int(input())
#kokku-=kommid
#print("Nüüd kokku on",kokku)

#print("Hello Мир!".center(75,"-")) #текст по центру то, что в "" знаки которые будут заполнять пустоту либо пробел
#nimi=input("Mis on sinu nimi? ").capitalize() #capitalize формат для большой буквы сначала по умолчанию akim->Akim
#print("Tere "+nimi+"!")
#print("Tere",nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled?"))          #"21"=21
#print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
#print ("Mutuja nimi=",nimi,type(nimi))   #обозначение класса переменной вместе с её значением
#print ("Mutuja vanus=",type(vanus))    #обозначение переменной без её значения. Влияет добавление значения ,nimi после "Mutuja vanus="

#arv1=float(input("Arv1: "))
#t=input("Tehe: ")
#arv2=float(input("Arv2: "))
#vastus=eval(str(arv1)+t+str(arv2))  #читает в формате текст, а выдаст в формате результата и преобразует 
#print("=",arv1,t,arv2,"=",vastus,sep="")  #sep="" убирает пробелы, либо какой-то символ
#print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus))


#vanus=18
#eesnimi="Jaak"
#pikkus=16.5
#kas_käib_koolis=True

#print("Muutuja vanus=",vanus,"on",type(vanus))
#print("Muutuja eesnimi=",eesnimi,"on",type(eesnimi))
#print("Muutuja pikkus=",pikkus,"on",type(pikkus))
#print("Muutuja kas_käib_koolis=",kas_käib_koolis,"on",type(kas_käib_koolis))

#u=float(input("Ümbermõõt: ")) #L=pi*2*r=pi*d
#d=round(u/pi,2) #round округление, первый символ значение чего, второй символ сколько цифр после запятой будет видно
#print("Läbimõõt =",d)

N = float(input("Sisesta ristküliku laius (N meetrites): "))
M = float(input("Sisesta ristküliku pikkus (M meetrites): "))
diagonaal = d**2=N**2 + M**2
print(f"Ristkülikukujulise maatüki diagonaal on {diagonaal:.2f} meetrit.")