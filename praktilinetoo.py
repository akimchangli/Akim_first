#eesnimi=input("Mis on sinu nimi?").capitalize()
#if eesnimi=="Juku":
#  try:
#      vanus=int(input("Kui vana sa oled?"))
#      print("Jukule ostame", end="")
#      if 0<vanus<=6:
#          print("tasuta pilet")
#      elif 6<vanus<=14:
#          print("lastepilet")
#      elif 14<vanus<=65:
#          print("täispilet")
#      elif 65<vanus<=100:
#          print("soodupilet")
#      else:
#          print("Viga andmetega!")
#  except:
#        print("Int andmetüüp on vaja kasutada!")
#else:
#    print("Mine ise kinno!")

#eesnimi = input("Sisesta esimese inimese nimi: ").capitalize() #"Eldar"
#teine_eesnimi = input("Sisesta teise inimese nimi: ").capitalize() #"Artur"
#if (eesnimi=="Eldar" and teine_eesnimi=="Artur") or (eesnimi=="Artur" and teine_eesnimi=="Eldar"):
#    print("Need on pinginaabri")
#else:
#    print("Rühmakaaslased")

#if  (eesnimi!=teine_eesnimi) and teine_eesnimi in ["Eldar, Artur"]:
#    print("Need on pinginaabri")
#else:
#    print("Rühmakaaslased")

#try:
#    pikkus=float(input("Pikkus"))
#    try:
#        laiusloatinput("Laius:")
#        S=pikkus*laius
#        print("Pindala võrdub",S)
#        soov=input("Kas tahad remondi teha?").lower() #jah, Jah, JAH --> jah upper()-->JAH
#        if soov=="jah" or soov=="да":
#            hind=float(input("Ruutmeetri hind: "))
#            summa=hind*S
#            print("Remondi suma on ", summa)
#        else:
#            print("Head aega")
#    except:
#     print("viga")
#except:
#    print("viga")

#try:
#    alghind = float(input("Sisesta alghind: "))
#   if alghind > 700:
#    soodustatud_hind = alghind * 0.7
#    print(f"30% soodustusega hind on: {soodustatud_hind:.2f}")
#   else:
#    print("Alghind ei ületa 700, seega soodustust ei rakendata.")
#except ValueError:
#    print("Viga! Palun sisesta arvuline väärtus.")
#    exit()

#   pikkus = float(input("sisetage inimese pikkus sentimeetrites:"))
#if pikkus < 160:
#   print("inimene on lühike")
#elif 160 <= pikkus <= 180:
#   print("inimene on keskmine pikkusega")
#else:
#   print("inimene on pikk")
#6-7
#sugu=input("Kas sa oled mees või naine?").lower()
#if sugu=="naine" or sugu=="n":
#    l1=155
#    l2=170
#    l3=255
#elif sugu=="mees" or sugu=="m":
#    l1=160
#    l2=180
#    l3=255
#else:
#    l1=0
#    print("Viga")
#if l1!=0:
#    try:
#        pikkus=int(input("Sisesta oma pikkus: "))
#        if pikkus>29 and pikkus<l1:
#            vastus= "lühike"
#        elif pikkus>=155 and pikkus<l2:
#            vastus="keskmine"
#        elif pikkus>=170 and pikkus<=l3:
#            vastus="pikk"
#        else:
#            vastus="tundmatu"
#        print("Sinu pikkus on {0}".format(vastus))
#    except:
#        print("Vale andmete formaat!")
#from random import*
#from datetime import*
##8
#arve_nr=datetime.now()
#tsekk="Arve:" +str(arve_nr)+ "\nToode Hind Kogus Summa\n"
#summa=0
#toode1="Piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toode1+" Hind"+str(hind)+"\n Kas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#toode1="Leib"
#hind2=randint(150,270)/100
#v=input("Toode:"+toode1+" Hind"+str(hind)+"\n Kas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#toode1="Kommid"
#hind2=randint(150,270)/100
#v=input("Toode:"+toode1+" Hind"+str(hind)+"\n Kas tahad osta?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode1+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#print (tsekk)
#try:
#    gender=input("Kas sa oled mees või naine?")
#    if gender.lower()=="naine":
#        print("Kahjuks, otsime ainult mehi")
#    else:
#        age=int(input("Palun märkige oma vanus"))
#    if age>=16 and <=18:
#        print("Sa sobid meie meeskonda!")
#    else:
#        print("Kahjuks sa ei sobi meie meeskonda.")
#except:

#hind = float(input("Sisesta toote hind: "))
#if hind <=10:
#    soodustus = hind*0,1
#else:
#    soodustus = hind*0,2
#okonnelik_hind = hind - soodustus
#print("Lõplik hind on", okonnelik_hind, "€")




#try:
#    s1=float(input("Введите длину первой стороны квадрата: "))
#    s2=float(input("Введите длину второй стороны квадрата: "))

#    if s1==s2 
#        print("Это квадрат!")
#    else:
#        print("Это не квадрат.")
#except: 
#    print("Где-то ошибка проверьте тип указанных данных!")

#a=10 #int
#b=2.3 #float
#c="programma" #str
#d="proga1" #str
#print(b.is_integer()) #false
#print(c.isalpha()) #true
#print(d.isalpha()) #false'
#print(d.isnumeric()) #false
#print(d.isdigit()) #digit
#print(d.isdecimal())
#print(d.is)

#try:
#    gender=input("Sugu: ")
#    if gender.isalpha() and (gender.lower()=="naine" or gender.lower()=="mees"):
#        if gender.lower()=="naine":
#            print("Ei soobi")
#        else:
#            try:
#                age=int(input("Vanus: "))
#                if 16<=age<=18:
#                    print("Oled meeskonnas!")
#                else:
#                    print("Vanuś ei soobi!")
#            except :
#                print("Vale vanus! Viga andmetüübiga!")
#    else:
#        print("Sisesta tekst!")
#except :
#    print("viga andmetüübiga!")'
    
#try:
#    print("Tere! Olen sinu uus sõber - Python!")
    
#    nimi = input("Sisestage oma nimi: ")
#    print(nimi + ", oi kui ilus nimi!")
    
#    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    
#    if vastus == 1:
#        pikkus = int(input("Sisestage oma pikkus (cm): "))
#        mass = float(input("Sisestage oma mass (kg): "))
        
#        indeks = mass / ((0.01 * pikkus) ** 2)
#        print(nimi + "! Sinu keha indeks on: {:.1f}".format(indeks))
        
#        if indeks < 16:
#            print("Tervisele ohtlik alakaal")
#        elif 16 <= indeks < 19:
#            print("Alakaal")
#        elif 19 <= indeks < 25:
#            print("Normaalkaal")
#        elif 25 <= indeks < 30:
#            print("Ülekaal")
#        elif 30 <= indeks < 35:
#            print("Rasvumine")
#        elif 35 <= indeks < 40:
#            print("Tugev rasvumine")
#        else:
#            print("Tervisele ohtlik rasvumine")
#    else:
#        print("Kahju! See on väga kasulik info!")
    
#    print("\nKohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
#except ValueError:
#    print("Viga! Palun sisestage õige arvuline väärtus.")

