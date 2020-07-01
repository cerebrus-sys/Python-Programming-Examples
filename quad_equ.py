'''
 ' Python program to solve a quadritic equation using quadritic formula.
'''

from cmath import sqrt

print("Format: a(x**2) + bx + c = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b*b)-(4*a*c)

print("X1 =", (-b-sqrt(d))/(2*a))
print("X2 =", (-b+sqrt(d))/(2*a))
