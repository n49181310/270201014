Year = int(input("Please enter the year: "))
x = Year
if Year%4 == 0 and Year%400 == 0:
  print(x,"is not leap year.")
elif Year%4 == 0:
  print(x,"is leap year.")
elif Year%4 != 0:
  print(x,"is not leap year.")