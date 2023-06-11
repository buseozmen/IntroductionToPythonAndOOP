benimListem = list()
type(benimListem)
#list

#instance & attribute
class SuperKahraman():
    ozelGuc = "Gorunmezlik"
    def __init__(self,isimInput,yasInput,meslekInput):
        print("init çağırıldı")
        self.isim = isimInput
        self.yas = yasInput
        self.meslek = meslekInput
    def ornekMethod(self):
        print(f"ben süperkahramanım ve mesleğim: {self.meslek}")
superman = SuperKahraman("Superman",30,"Gazeteci")
##self özelliklerin tanımlanmasına yardımcı oldu
superman.isim = "Clark Kent"
superman.ozelGuc = "uçabiliyor"
##değiştirebiliyoruz, zorunlu değil
superman.ornekMethod()

class Kopek():

    def __init__(self,yas = 5): #5 default
        self.yas = yas
    def insanYasiHesaplama(self):
        insanYasi = self.yas * 7
        print(f"Köpeğin insan yasi: {insanYasi}")
benimKopek = Kopek(4) #boş olursa ve default deger yok ise hata verir yas özelligini girmelisin
benimKopek.insanYasiHesaplama()

#inheritance
class Hayvan():
    def __init__(self):
        print("hayvan sınıfı çağırıldı")
    def method1(self):
        print("hayvan sınıfı method1 çağırıldı")
    def method2(self):
        print("hayvan sınıfı method2 çağırıldı")
benimHayvanim = Hayvan()
benimHayvanim.method1()
benimHayvanim.method2()

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sınıfı init çağırıldı")
    def miyavla(self):
        print("miyav")
    def method1(self):
        print("kedi sınıfındaki method1 çağırıldı") ##method1 hayvanda da var ama kedi sınıfından çağırılırsa burdan gelir
        #overrate
benimKedi = Kedi()
benimKedi.method1() #kalıtım aldığı için çağırılabiliyor
benimKedi.miyavla() #kedi hayvanın yaptığı her şeyi yapabilir ama hayvan kedinin yaptığı her eyi yapamaz.

#polymorphism
class Elma():
    def __init__(self,isim):
        self.isim = isim
    def bilgiVer(self):
        return self.isim + " 100 kaloridir "

class Muz():
    def __init__(self,isim):
        self.isim = isim
    def bilgiVer(self):
        return self.isim + " 150 kaloridir "
elma = Elma("elma")
elma.bilgiVer()
muz = Muz("muz")
muz.bilgiVer()

meyveListesi = [elma,muz]
for meyve in meyveListesi:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(muz)
bilgiAl(elma)

