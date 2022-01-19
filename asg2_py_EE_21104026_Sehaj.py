#question 1
x="Python is a case sensitive language"
print(len(x))  #a
print(x[::-1])  #b
print(x[10:27])  #c
z=x.replace("a case sensitive", "object oriented") #d
print(z)
y=x.index("a")   #e
print(y)
x=x.replace(" ", "") #f
print(x)

#question 2
Name = "Sehaj"
SID = "21104036"
Branch = "Electrical Enginerring" 
CGPA = "9.5"
x = "HEY, ABC Here! \n My SID is 2110XXXX \n I am from XYZ department and my CGPA is 9.9"
x = x.replace("ABC",  Name)
x = x.replace("2110XXXX", SID)
x = x.replace("XYZ", Branch)
x = x.replace("9.9", CGPA)
print(x)

#question 3
a = 56    #0b111000
b = 10    #0b1010
print(a & b)
print(a|b)
print(a^b)
print(a<<2) #11100000
print(a>>2) #001110
print(b<<2) #101000
print(b>>4) #0

#question 4
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = int(input("Enter third number : "))
if x>y>z  or x>z>y :
     print("The greatest number is : ", x)
elif y>x>z or y>z>x :
     print("The greatest number is : ", y)
else :
     print("The greatest number is : ", z)

#question 5
a = str(input("Write the rules regarding naming of variables in python : \n"))
b = "name" in a
if b == True:
    print("Yes")
else:
    print("No")

#question 6
a = int(input("Enter length of first side of triangle :"))
b = int(input("Enter length of second side of triangle :"))
c = int(input("Enter length of third side of triangle :"))
if a+b>=c and b+c>=a and c+a>=b:
    print("Yes")
else:
    print("No")