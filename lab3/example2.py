num1 = int(input("Enter the value 1: "))
num2 = int(input("enter the value 2: "))
num3 = int(input("Enter the value 3: "))
if num1 > num2 > num3:
  print(num3)
elif num3 > num2 > num1:
 print(num1)
elif num1 > num3 > num2:
  print(num2)