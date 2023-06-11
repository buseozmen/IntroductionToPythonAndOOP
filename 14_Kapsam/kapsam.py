#scope
numara = 20

def carpma(rakam):
    numara = 10 #local
    return numara * rakam
carpma(5) #50

print(numara) #20 verir global degisken

#Local,enclosing,global,built-in
benimAdim = "Buse"
#GLOBAL
def benimFonksiyonum():
    benimAdim = "Busra"
    #ENCLOSİNG
    def icFonksiyon():
        benimAdim = "Ceyda"
        #LOCAL
        print(benimAdim)
    icFonksiyon()
benimFonksiyonum()
print(benimAdim) #glabalde cagiriyor
##hiyerarşi var

y = 10
def yeniFonksiyon(y):
    print(y)
    y = 5
    print(y)
    return y
yeniFonksiyon(3)
y = yeniFonksiyon(3)
print(y)

y = 10
def ornekFonksiyon():
    global y
    y = 5
    print(y)
ornekFonksiyon()
print(y) #globali degistirdi



