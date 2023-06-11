x = 5
y = 4
print(x*y)
## 1.ornek

x = 6
print(x*y)
## en son atanan degeri tutar ona gore islem yapar

print(y*10)
## atanan degiskeni tutuyor

benimDegiskenim = 10
benimDigerDegiskenim = 20
print(benimDegiskenim + benimDigerDegiskenim)
print(type(benimDegiskenim))
sonuc = benimDegiskenim / benimDigerDegiskenim
print(type(sonuc))
## bolum olunca float verir (pythona özel)

a = 5
pi = 3.14
print(a*pi)
##float

x = 5
print(x**4)
## üslü ifade gosterimi

x = 10
print(x % 2)
##mod alma gosterimi

kullanicininYasi = input("Yasinizi giriniz.")
print(kullanicininYasi)
print(type(kullanicininYasi))
## kullanincininYasi string olarak algılanıyor

x = "merhaba dünya"
## daha önce int tanımlanan bir degisken sonradan str olarak tanımlanabilir (pythona özel)
print(type(x))
#cift tirnak da tek tirnak da kullanilabilir str de

benimString = "Buse Ozmen"
y = "yeni string"
print(benimString+y)
print(benimString*4)
#pythona özel ard arda 4 kez yazar

benimInput = input ("Yasinizi Giriniz :")
benimIntInput = int(benimInput)
print(type(benimIntInput))
## mantikli ise donusturur

k = "ozmen"
print(len(k))
##str karakter sayisini verir

isimString = "Buse Ozmen"
print(isimString[4])
##boslukta bir karakter
isimString[-1]
##son karakteri getir demek

yeniString = "0123456789"
print(yeniString[2:])
##ilk 2 elemanı almıyor sonrasını alıyor
print(yeniString[:3])
##sadece ilk 3 elemanı alıyor (slicing (kesmek))
gelenVeri = "AhmetinYasi65"
gelenVeri[-2:]
##son iki karakteri alır
gelenVeri[2:4]
## me çıktısı verir 2 yi dahil eder 4 ü etmez
gelenVeri[::2]
##Amtnai5 2 de 1 atlayarak alıyor
gelenVeri[1:10:3]
#1 de başla 10 da dur 3 te bir say cıktısı : htY
gelenVeri[::-1]
##tersten yazar

benimIsmim = "buse"
benimIsmim.capitalize()
benimYeniIsmim = benimIsmim.capitalize()
##yeni degisken atamalısın
benimTamIsmim = "Buse Ozmen"
benimTamIsmim.split()
type(benimTamIsmim.split())
##liste
benimTamIsmim.upper()
##butun harfleri büyük harf yapar
benimSoyadim = "ozmen"
benimIsmim + " " + benimSoyadim
##bosluk atti



