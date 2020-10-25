
for i in range(1,1000):
    i = str(i)
    if len(i) == 3 and int(i[0]) + int(i[1]) + int(i[2]) < 9:
        print(i,end= " ")
    elif len(i) == 2 and int(i[0]) + int(i[1]) <9:
        print(i,end= " ")
    elif len(i) == 1 and int(i[0]) <9:
        print(i,end= " ")
            
            
