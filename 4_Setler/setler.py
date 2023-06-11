benimListem = [1,2,3,1,2,3]
print(benimListem)
## listede aynı elemandan birden fazla olmasına izin veriliyor
benimListeSetim = set(benimListem)
print(type(benimListem))
print(type(benimListeSetim))
print(benimListeSetim)
##set'leyince birden çok olan verileri bire indiriyor

benimSet = {"a","b","c","a"}
print(benimSet)
bosListe = [ ]
print(type(bosListe))
bosListe.append(1)
print(bosListe)
bosSozluk = { }
print(type(bosSozluk))
##dict verir
bosSozluk["anahtarKelime"] = 10
print(bosSozluk)
benimBosSetim = set()
##set sınıfından oluşturulacak demek (diğer koleksiyon için de kullanılabilir)
benimBosSetim.add(10)
benimBosSetim.add(10)
benimBosSetim.add(20)
print(type(benimBosSetim))
print(benimBosSetim)
##ikinci 10 u saymıyor

