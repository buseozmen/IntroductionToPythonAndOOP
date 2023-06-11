def bolmeIslemi(numara):
    return numara / 2 #return olduğu için bir değişkenede eşitlenebiliyor
print(bolmeIslemi(20))

benimListem = [1,2,3,4,5,6,7,8,9,10]
yeniListe = []
for eleman in benimListem:
    yeniListe.append(bolmeIslemi(eleman))
print(yeniListe)

#map
list(map(bolmeIslemi,benimListem))
print(list(map(bolmeIslemi,benimListem)))

def kontrolFonksiyonu(string):
    return "a" in string

print(kontrolFonksiyonu("atil"))

stringListesi = ["buse","ozmen","polat","nurdan","ozgur","busra","ceyda","mehmet"]
sonucListesi = list(map(kontrolFonksiyonu,stringListesi))
print(sonucListesi.count(True))
print(list(map(kontrolFonksiyonu,stringListesi)))

#filter
print(list(filter(kontrolFonksiyonu,stringListesi)))
#true olanları gösteriyor

#lambda
carpma = lambda numara : numara * 3 #tek satırda yazmak için
carpma(10)

ornekListesi = [10,20,30]
list(map(lambda numara : numara * 4,ornekListesi))
print(list(map(lambda numara : numara * 4,ornekListesi)))



