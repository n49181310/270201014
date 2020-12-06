a = int(input("How many Fibonacci numbers to generate? "))
b = 0
c = 1
d = 1
print(c)
while a > 1:
  for i in range(a-1):
    b = c + d
    c = d
    d = b
    print(c)
  break