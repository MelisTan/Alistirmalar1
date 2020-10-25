
kalanlar=[]
bolenler = []

for x in range(1,126):
    if 125%x == 200% x == 350%x:
        bolenler.append(x)
        kalanlar.append(125%x)
           
        
for a in range(0,len(bolenler)):                 
    if kalanlar[a] == max(kalanlar):
        print(bolenler[a])                
        
               
                 
               
               
       
