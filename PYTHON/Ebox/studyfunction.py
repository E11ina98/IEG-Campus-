# inbuilt
# user-defined

# def sumOfTwoNumber(a,b):  


def mul(x,y):
    print("inside mul function")
    f = x*y
    return f


def sum_of_two_numbers(a,b):
    print("inside sum function")
    c = a +b
    d = mul(c,b)
    return d    # default return value is None

print("inside main")
a= 5
b= 10
c = sum_of_two_numbers(a,b)  #function call
f = mul(c,b)
print("sum=" ,c)

# recursion
#- a function calling a copy itself

# def fun(args):
#   if (base/ exit condition):
#   stmts
#   return

#   recursive call/calls

"""
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

n= int(input())
f= fact(n)
print(f)

"""

"""
fibonacci

0 1 1 2 3 5 8 13 21 ....
0 1 2 3 4 5 6 ....

n == 0 0
n == 1 1

f(n) = f(n-1) +f (n-2)


"""
"""
def fib(n):
    if n==0 or n==1 : return n
    return fib(n-1 + fib(n-2))

n= int(input())
print(fib(n))
"""
"""
combination
nCr = n!/(r!*(n-r))
nCr = (n-1)Cr + (n-1)C(r-1)

6C4 = 5C4 + 5C3


"""
def comb(n,r):
    if r == n or r == 0: return 1
    if r==1: return n
    return comb(n-1,r) + comb(n-1,r-1)

n = int(input())
r = int(input())

"""
def sum(b,a):
    print("a=",a)
    print("b=",b)
    c= a+b
    return c

x=5
y=10
d = sum (a=x, b=y)
print(d)
"""
def sum(a,b=10):
    c= a+b
    return c

x=5
c= sum (x)
print("sum =",c)
d= sum(x,20)
print("sum= ",d)