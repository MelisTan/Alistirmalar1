
for i in range(1000,2005):
    binler = i //1000  
    yuzler =  (i%1000) // 100    
    onlar = (i%100) // 10    
    birler = i%10
    
    if (binler+yuzler+onlar+birler) == (2005 - i):
        print(i)
    
