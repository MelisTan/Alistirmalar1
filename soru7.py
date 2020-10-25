sum = 0
for i in range(100,1000):
    i = str(i)
    if int(i[0]) + int(i[1]) == int(i[2]):
        sum += 1
        print(i, end= " ")

print("\n"+ str(sum) + " adet sayı bu koşulu sağlar.")        
        
