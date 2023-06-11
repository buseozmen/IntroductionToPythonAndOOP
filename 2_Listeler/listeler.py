benimString = "Buse Ozmen"
benimString[0]
## B
##benimString[0] = "A"
## bu mümkün degil degistiremezsin

benimListem = [10,20,10,40]
print(type(benimListem))
benimListem[0] = 100
##hata vermez mümkündür
benimListem.append(50)
##ekleme

benimNumaram = 10
benimDigerNumaram = 20
benimNumaraListem = [benimNumaram,benimDigerNumaram]
print(benimNumaraListem[0])

benimListem.pop()
##son elemanı atar
benimListem.remove(40)
##içeriğinden şunu sil
benimListem.count(20)
##20 den kaç tane var
benimDigerListem = ["buse","memo","ebu"]
##benimDigerListem[3]
##3. index yok hata verir

benimStringListem = ["nurdan","polat","ozgur"]
benimToplamaListem = benimStringListem + benimDigerListem
print(benimToplamaListem)
##python iki listeyi toplamaya izin veriyor

print(benimStringListem *5)
## buna izin verir bölüye vermez çünkü mantıksız

benimToplamaListem.reverse()
##ters çevirdi

karisikListe = [1,2,3.5,"buse",9]
type(karisikListe)
##list verir

sonucum = karisikListe[3]
type(sonucum)
##str verir

nestedList = [1,5,"buse",4,[6,"z"]]
type(nestedList)
##list verir
print(nestedList[4])
##[6,"z"]

zDegiskenimiz = nestedList[4][1]
print(zDegiskenimiz)

nestedList[:2]
##1,5
type(nestedList[:2])
##list
type(nestedList[2])
## str








