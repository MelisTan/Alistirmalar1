farklar = []
sayi1 = []
sayi2 = []

for a in range(1,1000):
    x = a
    for b in range(1,1000):
        y = b        
        if x*y == 121212:
            sayi1.append(x)
            sayi2.append(y)
            if (x-y) > (y-x):
                farklar.append(x-y)
            else:
                farklar.append(y-x)


for i in range(0,len(farklar)):
    if farklar[i]== min(farklar):
        print(sayi1[i] ,"\t",sayi2[i])
        
            
