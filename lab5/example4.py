pw="ab123"
help = "help"
while (True):
  pw2= input("Enter password: ")
  if (help == pw2):
    print("a")
  elif (pw == pw2):
    print("Welcome")
    break
  elif (pw != pw2):
    print("Wrong")