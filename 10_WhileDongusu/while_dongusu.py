x = 0
while x < 10:
    print(x)
    x = x + 1

benimListem = [1,2,3,4,5]
benimListem.pop() #son elemanı attı
print(benimListem)
benimListem.append(5)
print(benimListem)
while 3 in benimListem: #3 bu listenin içinde olduğu sürece çalışacaktır
    print("3 hala listenin içerisinde")
    benimListem.pop()

numara = 0
while numara < 5:
    if numara == 4:
        break
    print(numara)
    numara = numara + 1

yeniDegisken = 0
while yeniDegisken < 15:
    ##print("yeniDegiskenin güncel degeri : ", yeniDegisken) virgül yerine artı koyarsak hata verir
    print(f"yeniDegiskenin güncel degeri : {yeniDegisken}")
    yeniDegisken = yeniDegisken + 1



