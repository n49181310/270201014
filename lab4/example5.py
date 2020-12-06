a = int(input("Please enter a number: "))
fact = 1
while True:
  if a < 0:
    print("Please enter the positive number")
  elif a > 0:
    for i in range(1,a+1):
      fact *= i
  break
print(fact)

