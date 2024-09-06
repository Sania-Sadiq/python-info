print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Division")
option = int(input("Choose an operation:"))

if(option in [1,2,3,4]):
    num1= int(input("Enter the first number:"))
    num2= int(input("Enter the second number:"))
    
    if(option == 1):
        results = num1 + num2
        print(results)
    elif(option == 2):
        results = num1 - num2
        print(results)
    elif(option == 3):
        results = num1 * num2
        print(results)
    elif(option == 4):
        results = num1 // num2
        print(results)
else:
    print("Invalid operation entered")       


