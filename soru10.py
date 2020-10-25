sum= 0
for i in range(10000,100000):
    i = str(i)
    if i[0] == i[3] and i[1]== i[4]:
        sum += 1
       
print(sum)        
