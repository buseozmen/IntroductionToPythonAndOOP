benimListem = [10,20,30,40,50]
if 10 in benimListem:
    print("evet")
benimListem[0]*5/3
benimListem[1]*5/3
## bütün elemanlar için tek tek yapmak zor olur

print("dongu basladi")
for numara in benimListem: #sırasıyla numara degiskenine atiyor
    print(numara * 5 / 3)
print("dongu bitti")

for num in benimListem:
    yeniNumara = num * 5 / 3
    print(yeniNumara)

yeniListe = [1,2,3,4,5,6]
for rakam in yeniListe:
    if rakam % 2 == 0:
        print(rakam)

yeniString = "Buse Ozmen"
for harf in yeniString:
    print(harf)

benimTuple = (1,2,3,4,5)
for eleman in benimTuple:
    print(eleman - 10)

koordinatListesi = [(10.2,15.2),(32.4,16.2),(40.2,20.2)]
print(type(koordinatListesi[0]))
for eleman in koordinatListesi:
    print(eleman)

for (x,y) in koordinatListesi:
    print((y))

benimGaripListem = [(1,2,3),(4,5,6),(7,8,9)]
for (x,y,z) in benimGaripListem:
    print(z)

benimSozluk = {"muz" : 150, "portakal" : 250, "elma" : 400}
print(benimSozluk.items())
print(type(benimSozluk.items())) #dict_items diye sınıflandırıyor

for (anahtar,deger) in benimSozluk.items():
    print(anahtar)

for (anahtar,deger) in benimSozluk.items():
    print(deger)