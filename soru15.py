
for n in range(10000,100000):
    asalmi = True
    for x in range(2,n):
        if n%x == 0:
            asalmi = False
            break
        
    if asalmi == True:
        print(n,end = " ")

# 2nd Way
        
for n in range(10000,100000):
    for x in range(2,n):
        if n%x == 0:
            break        
    else:
        print(n,end = " ")
