num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 * num2

print(str(num1) + " * " + str(num2) + " = "+str(result))
if(result > 0) :
    print("The result is positive.")
elif (result < 0) :
    print("The result is negative.")
elif (result == 0): 
    print("The result is positive and negative.")
else : 
    print("incorrect input")