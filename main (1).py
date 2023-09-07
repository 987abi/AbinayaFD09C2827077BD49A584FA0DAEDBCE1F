#python program to find the factorial of a number using recursion
#fact _recur.py
def fact(m):
 if m<=1:
  return 1
 else:
  return m*fact(m-1)
n=int(input("Enter the value ofn: "))
print("The factorial of",n,"is",fact(n))
