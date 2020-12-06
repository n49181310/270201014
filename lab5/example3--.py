a = input("Please enter an integer: ")
b = input("Please enter an integer: ")
count=0
a = str(a)
b = str(b)
for i in range(len(a)):
  if a[i] == b[i]:
    count+=1
print(count)