# test
x = 5
print(x)

def Add(x,y):
  return x + y
def Subtract(x,y):
  return x - y
def Multiply(x,y):
  return x * y
def Divide(x,y):
  return x / y
def Exponent(x,y):
  return x ** y

print("WHAT YOU TRYN DO")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")

result = int(input("Which one (1/2/3/4/5): "))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if result == 1:
  print(x, "+", y, "=", Add(x,y))
elif result == 2:
  print(x, "-", y, "=", Subtract(x,y))
elif result == 3:
  print(x, "*", y, "=", Multiply(x,y))
elif result == 4:
  print(x, "/", y, "=", Divide(x,y))
elif result == 5:
  print(x, "TO THE POWER OF", y, "=", Exponent(x,y))
else:
  print("WRONG ANSWER MF")
