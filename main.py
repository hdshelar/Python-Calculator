#CLACULATOR

print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n")
num = int(input("select any option:"))

if num == 1:
    num1 = int(input("enter number one:"))
    num2 = int(input("enter number two:"))
    def add(num1,num2):
        return num1+num2
    print(add(num1,num2))
elif num == 2:
    num3 = int(input("enter number one:"))
    num4 = int(input("enter number two:"))
    def sub(num3,num4):
        return num3-num4
    print(sub(num3,num4))
elif num == 3:
    num5 = int(input("enter number one:"))
    num6 = int(input("enter number two:"))
    def div(num5,num6):
        return num5/num6
    print(div(num5,num6))
elif num == 4:
    num7 = int(input("enter number one:"))
    num8 = int(input("enter number two:"))
    def mul(num7,num8):
        return num7*num8
    print(mul(num7,num8))
else:
    ("Select valid option !")