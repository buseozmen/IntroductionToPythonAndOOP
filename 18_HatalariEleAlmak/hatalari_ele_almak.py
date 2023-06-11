def toplama(numara1,numara2):
    return numara1 + numara2
x = int(input("İlk numarayı giriniz: "))
y = int(input("İkinci numarayı giriniz: "))
toplama(x,y)
#x e veya y ye int yerine str girilirse hatayı ele almalıyız

#try & except & else & finally
while True:
    try:
        benimInt = int(input("Numaranızı giriniz: "))
    except:
        print("Lütfen gerçekten numara giriniz")
        continue
    else:
        print("teşekkürler")
        break
    finally:
        print("finally çağırıldı")