benimListem = [1,2,"a",4.5]
print(benimListem[0])
benimListem[0] = 100
print(benimListem)
##değiştirildi

benimTuple = (1,2,"a",4.5)
print(benimTuple)
benimTuple[0]
##1
##benimTuple[2] = "b"
##değiştirilemez

benimTuple.count("a")
##1
benimTuple.index(4.5)
##3
