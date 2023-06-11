class Meyve():

    def __init__(self,isim,kalori):
        self.isim = isim
        self.kalori = kalori

    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"

    def __len__(self):
        return self.kalori
muz = Meyve("Muz",150)

print(muz) ##str fonk.
#<__main__.Meyve object at 0x000002174309F090>
benimListem = [1,2,3,"a",4.5]
print(benimListem)
len(benimListem)
print(len(muz)) #len fonk. olmasa hata verirdi

elma = Meyve("Elma",200)
print(len(elma))
print(elma)

##özel methodları special methods in python (magic methods) diye aratabilirsin