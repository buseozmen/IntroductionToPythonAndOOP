benimAdim = "Buse Ozmen"
print(benimAdim.upper())

print(benimAdim)
benimAdimBuyuk = benimAdim.upper()
print(benimAdimBuyuk)

def ilkFonksiyon():
    print("ilk fonksiyonum")
ilkFonksiyon() #çalışması için çağırmak gerek

##input & return
def merhabaDunya(yazdirilacakIsim):
    print("merhaba")
    print(yazdirilacakIsim)
merhabaDunya("Buse")

def merhaba(isim = "buse"):
    print("merhaba")
    print(isim)
merhaba()
merhaba("busra")

def toplama(numara1,numara2):
    sonuc = numara1 + numara2
    print(sonuc)
toplama(-200,350)

def superToplama(num1,num2,num3):
    print(num1+num2+num3)
superToplama(10,20,30)

yeniDegisken = toplama(10,20)
print(yeniDegisken) #none çıktısı verir çünkü fonk. deger döndürmüyor

def dondurmeliToplama(num1,num2):
    return num1+num2
yeniSonuc = dondurmeliToplama(10,20)
print(type(yeniSonuc))

def kontrolFonksiyon(s):
    if s == "buse":
        print("verdiğiniz string buse")
    else:
        print("verdiğiniz string başka bir şey")
kontrolFonksiyon("buse")
kontrolFonksiyon("ozgur")

##args & kwargs
def yeniToplama(*args):
    return sum(args)

print(yeniToplama(10,20,30,40))

def benimFonksiyonum(*args):
    print(args)
print(type(benimFonksiyonum(20,30,40))) ##nonetype

def benimFonksiyonum(*args):
    return(args)
print(type(benimFonksiyonum(20,30,40))) ##tuple

def ornekFonksiyon(**kwargs):
    print(kwargs)
ornekFonksiyon(muz = 100, elma = 200, ananas = 300)
print(type(ornekFonksiyon(muz = 100, elma = 200, ananas = 300)))
##nonetype

def ornekFonksiyon(**kwargs):
    return(kwargs)
ornekFonksiyon(muz = 100, elma = 200, ananas = 300)
print(type(ornekFonksiyon(muz = 100, elma = 200, ananas = 300)))
##dict

def keyWordKontrolu(**kwargs):
    if "buse" in kwargs:
        print("buse var")
    else:
        print("buse yok")

keyWordKontrolu(busra = 70, ceyda = 50, nurdan = 80)



