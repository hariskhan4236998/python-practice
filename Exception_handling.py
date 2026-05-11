##Exception handling Example 1
name = 'haris'
try:
    name = int(name)
except:
    name = 1
print("hello",name)

##Exception handling Example 2
x = '345'
y = "hello"
try:
    x = int(x)
except:
    y = int(y)
print(x,y)


##Exception handling Example 3
number = input("Enter a Number")
try:
    num = int(number)
except:
    num = -1
if num > 0:
    print("Great work")
else:
    print("input number")

#Exception handling Example 4
try:
    x = float(input("Enter your cgpa:"))
    print("your Cgpa is =",x)
except ValueError:
    print("Please Enter your CGPA in numbers ....!")
