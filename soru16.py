
num = int(input("enter a number:\t"))

for a in range(2,num):
    if num%a == 0:
        print("This is not a prime number.")
        break
else:
    print("This is a prime number.")
    
