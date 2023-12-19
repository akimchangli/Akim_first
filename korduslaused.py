arv=int(input("Sisesta arv: "))
if arv==13:
    arv=77
print(arv)


if arv>0:
    print("Positiivne arv")
elif arv<0:
    print("Negatiivne arv")
else:
    print("Ei saa arvestada")


hinne=input("Mis hinne sa täna sai?") #A MA X
if hinne=="5" or hinne=="A":
    print("Tubli!")
elif hinne=="4":
    print("Hea hinne!")
elif hinne=="3":
    print("Rahuldav!")
elif hinne=="2" or hinne=="1" or hinne=="MA":
    print("Halb!")
elif hinne=="X":
    print("On vaja töö soritada")
else:
    print("Ma ei tea, mis hinne see on!")


from random import *
a=randint(-1000,1000)
print(a)
if a%3==0:
    print("{0} jagatakse kolmega".format(a))
else:
    print("Ei saa jagada kolmega")

from random import *
vanus=randint(14,23)
print(vanus)
if vanus>=18:
    print("Täiskasvanud inimene. Vanemad ei saa kontrollida tulemusi")
else:
    print("Vanemad kontrollivad lapsi")
