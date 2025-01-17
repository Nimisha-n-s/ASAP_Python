num=int(input("Enter a three digit number: "))
result=0
temp = num

while temp != 0:
    rem = temp%10
    result = result + rem * rem * rem
    temp = temp//10

if result == num:
    print("It is an amgstrong number")
else: 
    print("It is not an amgstrong number")
