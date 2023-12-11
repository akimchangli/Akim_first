#print("Hello Мир!".center(75,"-")) #текст по центру то, что в "" знаки которые будут заполнять пустоту либо пробел
#nimi=input("Mis on sinu nimi? ").capitalize() #capitalize формат для большой буквы сначала по умолчанию akim->Akim
#print("Tere "+nimi+"!")
#print("Tere",nimi+"!")
#print("Tere {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled?"))          #"21"=21
#print("Tere {0}! Sa oled {1} aastat vana".format(nimi,vanus))
#print ("Mutuja nimi=",nimi,type(nimi))   #обозначение класса переменной вместе с её значением
#print ("Mutuja vanus=",type(vanus))    #обозначение переменной без её значения. Влияет добавление значения ,nimi после "Mutuja vanus="

arv1=float(input("Arv1: "))
t=input("Tehe: ")
arv2=float(input("Arv2: "))
vastus=eval(str(arv1)+t+str(arv2))  #читает в формате текст, а выдаст в формате результата и преобразует 
print("=",arv1,t,arv2,"=",vastus,sep="")  #sep="" убирает пробелы, либо какой-то символ
print("{0}{1}{2}={3}".format(arv1,t,arv2,vastus)) 