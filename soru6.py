sum = 0
for i in range(1000,10000):
    i = str(i)
    if i[0] > i[3]:
        sum += 1
print(sum)
