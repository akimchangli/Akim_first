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

try:
    alghind = float(input("Sisesta alghind: "))
   if alghind > 700:
    soodustatud_hind = alghind * 0.7
    print(f"30% soodustusega hind on: {soodustatud_hind:.2f}")
   else:
    print("Alghind ei ületa 700, seega soodustust ei rakendata.")
except ValueError:
    print("Viga! Palun sisesta arvuline väärtus.")
    exit()
