benimBoolean = True
print(type(benimBoolean))
listem = [5000,10000,3000,1000,2000,4000]
print(len(listem))
print(sum(listem))
ortalama = sum(listem) / len(listem)
print(ortalama)
sonuc = listem[3] > ortalama
print(sonuc)
##false
print(type(sonuc))
##bool
kullaniciMaas = input("maas bilgisini giriniz: ")
kullaniciMaasInt = int(kullaniciMaas)
sonuc2 = kullaniciMaasInt > ortalama
print(sonuc2)

x = 10
y = 8
##x >= y true
##9 >= 9 true
##x <= y false
##x = y yapmak x i y ye eşitler
##x == y dersek eşit mi diye kontrol etmiş oluruz
##x != y x eşit değil y ye
##3>1 and 3>2 true verir
##1>3 or 3>2 true verir
##not 5 == 5 false verir