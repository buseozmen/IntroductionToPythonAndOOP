if 3 > 1:
    print("buseozmen")
    print("if koşulu sağlandı")
print("if koşulunun dışına çıktık") #her türlü çalışcak

x = 4
y = 4
if x > y:
    print("x, y den daha büyüktür")
elif y > x: #else if kısaltımı
    print("y, x den büyüktür")
else:
    print("x ve y birbirine eşittir")

benimKahramanım = input("Super kahraman seciniz: ")
if benimKahramanım == "batman":
    print("batmani sectiniz tebrikler")
elif benimKahramanım == "superman":
    print("keske batmani secseydiniz")
elif benimKahramanım == "ironman":
    print("ironman kimdir ?")
else:
    print("bu kim gerçekten bilmiyoruz")

a = 10
b = 20
c = 30
if a > b and b > c:
    print("a, b den büyük ve b de c den büyüktür")
elif a < b and b < c:
    print("a,b den küçük ve b de c den küçüktür")
else:
    print("bu koşullar tutmadı")

karakterCanli = True
if karakterCanli == True:
    print("oyun karakteriniz yasiyor")
else:
    print("oyun karakteriniz yasamiyor")

if karakterCanli: # bool degiskenler için bu sekilde yazilabilir
    print("oyun karakteriniz yasiyor")
else:
    print("oyun karakteriniz yasamiyor")

if not karakterCanli:
    print("karakter canli degil")

benimString = "Buse Ozmen"
if benimString == "buse ozmen":
    print("eşitmiş")
else:
    print("yokmuş")
##stringlerde büyük harf küçük harf önemli
if "Ozmen" in benimString:
    print("varmış")
else:
    print("yokmuş")

benimListem = [10,20,30,40,50]
if 60 in benimListem:
    print("evet var")

benimSozluk = {"muz" : 100, "elma" : 150, "karpuz" : 500}
if "muz" in benimSozluk: #benimSozluk.keys(): de denilebilir
    print("varmış")
if 500 in benimSozluk.values():
    print("evet")

