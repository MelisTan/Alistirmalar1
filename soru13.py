
for a in range(10,100):
    x = a
    for b in range(10,100):
        y = b
        num = int(str(x)+str(y))
        if num == (x+y)*11:
            print("x =" ,str(x) ,"\ny =", str(y))

        
