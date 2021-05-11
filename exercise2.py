print("Faulty Calculator")
a = int(input("Enter the number:"))
b = int(input("Enter 2 the number:"))
print("enter the basic operations:\n1 addition\n2 subtraction \n3 Multiplication \n4 Division")
operation = int(input("Choose your operation:"))
if a==56 and b==9 and operation==1:
    print(555)
elif a==32 and b==12 and operation == 2:
    print("Subtraction is:",89)
elif a==45 and b == 3 and operation == 3:
    print("Multiplication is :",555)
elif a==56 and b == 7 and operation == 4:
    print("Division is :",4)
# this is for random selection
elif operation == 1:
    print("addition is:",a+b)
elif operation == 2:
    print("Subtraction is:",a-b)
elif operation == 3:
    print("Multiplication is: ",a*b)
elif operation == 4:
    print("division", a / b)
else:
    print("Invalid operations...")