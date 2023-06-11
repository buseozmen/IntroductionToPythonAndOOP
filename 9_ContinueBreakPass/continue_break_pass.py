benimListem = [5,10,15,20,25,30]
for numara in benimListem:
    print(numara/5)

for numara in benimListem:
    if numara == 15:
        break
    print(numara) #devam etmez

for numara in benimListem:
    if numara == 15:
        continue
    print(numara) #numarayı atlıyor ve devam ediyor

for numara in benimListem:
    pass #geçici süreliğine kullanılabilir