benimListem = [1,2,3]
benimListem[0]
##çıktı : 1 (listeler için)

benimYemeklerim = ["elma","karpuz","muz"]
benimKalorilerim = [100,200,300]
## ikisinin eşleşmesinde sıkıntı olabilir o yüzden mantıklı değil
## sözlük devreye girer

benimSozluk = {"anahtarkelime" : "deger"}
print(type(benimSozluk))
## dict
##print(benimSozluk[0])
## hata verir
print(benimSozluk["anahtarkelime"])
##deger

benimYemekKaloriSozlugum = {"elma" : 100, "karpuz" : 200, "muz" : 300}
benimYemekKaloriSozlugum["muz"]
##300
benimYemekKaloriSozlugum["elma"] = 200
print(benimYemekKaloriSozlugum)
## değiştirilebiliyor
benimDegisikSozlugum = {150:"nurdan",-2:"ozgur"}
print(benimDegisikSozlugum[-2])
##anahtar kelime her şekilde olabilir
yeniDictionary = {"anahtar1":100,"anahtar2":[10,20,30,40,4.5,"buse"],"anahtar3":{"anahtar9":4}}
yeniDictionary.keys()
##anahtar kelimeleri verir bir liste içerisinde
yeniDictionary.values()
##degerleri verir
print(yeniDictionary["anahtar2"][5])
print(yeniDictionary["anahtar3"]["anahtar9"])
##index yerine anahatr kelime kullanılır listeyle aynı mantık
