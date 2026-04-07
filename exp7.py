#Define and call a function
def greet():
    print("Welcome to python")
greet()


#Pass arguments to function
def add(a, b):
    print("Sum of the numbers: ", a+b)
add(8,9)


#Return multiple values
def calc(a,b):
    return a+b, a-b
x,y=calc(50,10)
print("Sum of the numbers: ",x)
print("Difference of the given numbers: ",y)


#Factorial using function
def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
print("Facorial: ", fact(5))


#Factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print("Factorial by using recursion is: ", fact(5))


#Fibonacci series using rescursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print("Fabonacci series is: ")
for i in range(6):
    print(fib(i), end="\n")
    
    
#Lamda function
square= lambda x: x*x
print("Square is: ", square(5))


#Built in functions
l=[5,9,4,7,6]
print("Sum: ",sum(l))
print("length: ", len(l))
print("Maximum: ", max(l))
print("Minimum: ", min(l))


#Scope of the variables
x=10          #global
def test():
    x=5        #local
    print("Local variable: ", x)
test()
print("Global variable: ",x)


#Prime numbers using functions
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
      if n%i==0:
        return False
    return True
n=int(input("Enter the number: "))
if is_prime(n):
    print("Prime")
else:
    print("Non-prime")