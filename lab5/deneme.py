a = input("Please enter an integer: ")
b = input("Please enter an integer: ")
count = 0
b = str(b)
for i in range(len(str(a))):
  if a[i] == b[i]:
    count +=1
print(count)