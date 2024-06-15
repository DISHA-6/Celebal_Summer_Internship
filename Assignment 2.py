#Create a simple calculator which can perform simple arithmetic operations like add, subtract, division, multiplication etc.
def add(a,b):
  return a+b
def substract(a,b):
  return a-b
def multiplication(a,b):
  return a*b
def division(a,b):
  if b != 0:
   return a/b
  else:
   return "Error!! Division by zero cannot be done!!"


while True:

    print("Select operation: ")
    print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
    choice=input("Enter choice(1 or 2 or 3 or 4): ")

    if(choice in ('1','2','3','4')):
      try:
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
      except ValueError:
        print("Invalid input!! Please enter a valid number n!!")
        continue

      if choice == '1':
        print(a,"+",b,"=", add(a,b))
      elif choice == '2':
        print(a,"-",b,"=", substract(a,b))
      elif choice == '3':
        print(a,"*",b,"=", multiplication(a,b))
      elif choice == '4':
        print(a,"/",b,"=", division(a,b))
      next_cal = input("Wnat to do next calculation? (y/n): ")
      if next_cal == "n":
        break
      else:
        print("Invalid input!\n")
        
    else:
        print("Invalid input!!")