num = input("Enter a number.")
if len(num) == 4 or len(num) == 3:
    if num == num[::-1]:
        print("This is a palindromic number")
    else:
        print("This is not a palindromic number")
else:
    print("Please enter a three or four digit number!")
        
        

