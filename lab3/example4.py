age = int(input("Enter your age: "))
if age < 6 or age > 60:
  print("Your ticket is free")
elif 60 > age > 18:
  print("Your ticket is 3 TL")
elif 6 < age < 18:
 print("Your ticket is 1.5 TL")