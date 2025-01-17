print("Enter two numbers")
a=int(input("a = "))
b=int(input("b = "))

print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4.Division")
ch=int(input("\nEnter choice: "))

if ch==1:
    print("Sum = ", a+b)
elif ch==2:
    print("Difference = ", a-b)
elif ch==3:
    print("Product = ", a*b)
elif ch==4:
    print("Quotient = ", a/b)
    