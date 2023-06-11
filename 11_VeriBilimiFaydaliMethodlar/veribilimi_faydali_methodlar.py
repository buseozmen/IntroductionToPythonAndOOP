#range
print(list(range(15))) #(0,15) arası
for numara in list(range(15)):
    print(numara*5)

print(list(range(5,22,4))) #5 den başla 22 ye kadar 4 er atlayarak

#enumerate
index = 0
for numara in list(range(5,15)):
    print(f"güncel numara: {numara} güncel index: {index}")
    index = index + 1

for eleman in enumerate(list(range(5,15))):
    print(eleman)
#bir önceki işlemin enumerate komutu ile yapılması

for (index,numara) in enumerate(list(range(5,15))):
    print(numara)

#random
from random import randint
print(randint(0,100))

yeniListe = list(range(0,10))
print(yeniListe)
random = yeniListe[randint(0,9)]
print(random)

#shuffle
from random import shuffle #karistirma
shuffle(yeniListe)
print(yeniListe)

#zip
yemekListesi = ["muz","ananas","elma"]
kaloriListesi = [100,200,300]
gunListesi = ["pazartesi","salı","çarşamba"]
ziplenmisListe = list(zip(yemekListesi,kaloriListesi,gunListesi))

for eleman in ziplenmisListe:
    print(type(eleman))

print(ziplenmisListe)

#listeler ileri seviye
listeOrnegi = []
benimString = "buse ozmen"

for harf in benimString:
    listeOrnegi.append(harf)
print(listeOrnegi)

yeniString = "buse ozmen"
yeniListeOrnegi = [eleman for eleman in yeniString]
print(yeniListeOrnegi)

ikinciListeOrnegi = [numara ** 5 for numara in list(range(0,10))]
print(ikinciListeOrnegi)
