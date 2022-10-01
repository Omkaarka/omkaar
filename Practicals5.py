#Write a function with return expression
#1) Take 12th 5 marks return total and percentage(return multiple values)
def a(v,w,x,y,z):
    total=v+w+x+y+z
    percent=total/5
    print(total,percent)
    return total, percent
a(80,90,100,89,92)
#2) To add 1-100(add)
def add(a):
    b=sum(range(1,a+1))
    print(b)
    return b
add(100)
#3) To find maximum of 3 numbers(max no.)
def great(a,b,c):
    g=max(a,b,c)
    m=min(a,b,c)
    print(g,m)
    return g, m
great(50,40,45)
#4) To reverse a number(Eg. 1234--->4321)
def rev(a,b,c,d):
    e=[a,b,c,d]
    e.reverse()
    print(e)
    return e
rev(1,2,3,4)
#5)To check given number is a palindrome or not.
def rev(a,b,c,d):
    e=[a,b,c,d]
    b=e[::-1]
    if e==b:
        print(e,' is a palindrome')
    return e
rev(1,2,2,1)

#Write function without return expression.
#1) Check a number odd or even
def num(a):
    if a%2==0:
        print(a,' is even number')
    else:
        print(a,' is odd number')
num(55)
'''2) To print a pattern
11111
2222
333
44
5'''
#3) Use nested if inside a function.
def marks(a):
    if a>=75:
        if a>89:
            print('you have above 90 percent')
        else:
            print('you have above 75 percent')
    else:
        print('you have below 75 percent')
marks(97)
#4) To check a number is prime or not
def num(a):
    for i in range(1,a+1):
        if i%a==0:
            print(i,' not a prime number')
        else:
            print(i,' is a prime number')
num(55)
#....
#5)Calculate area and circumference of a circle
def data(r):
    a=3.14*r*r
    print(a)
    c=3.14*2*r
    print(c)
    return a,c
data(7)
