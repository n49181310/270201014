x = int(input("How many numbers? "))
even_number=0
odd_number=0
for i in range(x):
  c = int(input("Enter an integer: "))
  if c%2==0:
    even_number +=1
  elif c%2==1:
    odd_number +=1
print("%", (even_number/(even_number+odd_number))*100)


