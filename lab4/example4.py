a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = 1
while b>0:
  for i in range(b):
    c *= a
  break
print(c)