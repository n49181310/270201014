print("ax2 + bx + c")
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))
Discriminant = b**2 - 4*a*c
xx1 = (-b + Discriminant**0.5)/2*a
xx2 = (-b - Discriminant**0.5)/2*a
xx3 = -b/2*a
if Discriminant > 0:
  print("First root is", xx1)
  print("Second root is", xx2)
elif Discriminant == 0:
  print("First root is", xx3)
  print("Second root is", xx3)
elif Discriminant < 0:
  print("There is not root")
