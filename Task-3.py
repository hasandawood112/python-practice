def divide(a, b):
    if a%b == 0:
        print("Number 1 is completly divisible by number 2!")
    else:
        print("Number 1 is not completly divisible by number 2!")


num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

divide(num1, num2)