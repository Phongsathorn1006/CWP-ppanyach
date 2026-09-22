num = int(input("Enter the number less than 25 : "))

if(num > 25) :
    print("Error")
elif(num < 25 and num > 0) :
    for i in range(num,26,1):
        print(f"Inside the loop, my variable is {i}")
# else : 
#     print("not correct input")