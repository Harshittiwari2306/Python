def factorial(a):
 if a < 0:
  return "The factorial is not possible"
 elif a== 1 or a== 0:
  return 1
 return a*factorial(a-1)

a = float(input("Enter a number : "))
print(f"factorial of {a} is {factorial(a)}")