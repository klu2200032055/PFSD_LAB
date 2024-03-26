
'''# Squaring of Numbers
n=int(input("Enter a number"))
if n==0:
    print("Wrong Input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)



# To print each character of the string in ascending and descending order
x=0
str1="thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])
for i in str1:
    x=x-1
    print(str1[0:x])



# Printing Pattert of * without spaces

x=int(input())
str1="*"
print('*')
for i in range(0,x-1):
    x=x+1
    str2='*'
    str1=str2+str1
    print(str1[0:x])

#Another Solution for * Patterns
# Program for printing "*" according to the given input

n=int(input("Enter number of astriks you need:"))
x=n
for i in range (n):
        print("*"*x)
        x=x-1
x=1
for i in range (n):
        print("*"*x)
        x=x+1


a1=int(input())
a2=format(a1,'b')
a3=format(a1,'o')
a4=format(a1,'x')
a5=input()
a6=int(format(int(a5,2),'d'))
print('In Binary',a2)
print('In Octal',a3)
print('In HexaD',a4)
print('bin to Int',a6)
'

#Ex-2 -1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

print("Factorial of {number}: {factorial(number)}")



#Ex-2-2
print("First 7 multiples of 7:")
for i in range(1, 8):
    print(7 * i)

#Ex-2-3
def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2

side_a, side_b, side_c = map(float, input("Enter lengths of three sides separated by space: ").split())

if is_right_triangle(side_a, side_b, side_c):
    print("It's a right triangle.")
else :
    print("It's not a right triangle.")

#Ex-2-4
n=int(input("Enter number of astriks you need:"))
x=1
for i in range (n):
        print("*"*x)
        x=x+1
x=n-1
for i in range (n):
        print("*"*x)
        x=x-1

#Ex-2-5
bS = input("Enter 4-binary digit numbers: ")
bN = bS.split(',')
dv5 = [binary for binary in bN if int(binary, 2) % 5 == 0]
print(','.join(dv5))


#VIVA Q2
numbers = [3, 6, 9, 12, 15]

for num in numbers:
    multiplied = num * 2
    print(multiplied)

'''























