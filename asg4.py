# ques 1
def TOH(n, source, destination, helperpole):
    if n== 1:
        print("Move disk 1 from source", source,"to destinaton",destination) #moving disk 3 to rod C
    else:
     TOH(n-1, source, helperpole, destination) #moving 2(1,2) disks to rod B
     print("Move disk", n, "from source", source, "to destination", destination)
     TOH(n-1, helperpole, destination, source)
n = 3
TOH(n , "A", "C", "B")

#  ques 2
# using iteration
n = int(input("Enter number of rows for Pascal's triangle : "))
if n ==0:
    print( )
else:
    for i in range(0,n):
            print(" "*(n-i), end= "")
            print(" ".join(map(str ,str(11**i))))
# using recursive method
n = int(input("Enter number of Rows: "))
def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)

def pasc(rows):
    for j in range(rows): #j = rows
        answer = ""
        for i in range(j+ 1): #i = columns
            answer += str(combination(j, i)) + "\t"
        print(answer)

pasc(n)

#ques 3
from pickle import NONE


num1 = int(input("Enter 1st number : "))
num2 =int(input("Enetr 2nd number : "))
print("Quotient obtained from the two numbers is : ", '%0.3f'%(num1/num2))
print("Remainder obtained from the two numbers is : ", '%0.3f'%(num1/num2))
#a
#num1 and num2 are not callable since they are normal variables
print(callable(num1)) 
print(callable(num2))
def x(): #by definig a function we can call num1 and num2
    x = num1
def y():
    y = num2
print(callable(x))
print(callable(y))
list =[ num1, num2, round(num1/num2, 2), round(num1%num2, 2)]
for i in range(0,2):
    if list[i] == 0 :
        print("given value is zero")
    else:
        print("Given value is non zero")
list1 = [4,5,6]
list = list + list1
print(list)
print("Values lesser than 4 ")
list2= []
for j in range(0,5 ):
    if list[j] < 4:
        a = list[j]
        print(a) #c
        list2.append(a)
print(list2)
y = set(list2)
print(y) #d converting to set datatype
yn = frozenset(y) #e yn is an immutable set 
print(max(y)) #f maximum value of set
print(hash(max(y))) #hash value for the maximum value 

#ques 
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno  = rollno

student1 = Student("Harry", 26)
student2 = Student("Ron", 56)
student3 = Student("Hermione", 15)
student4 = Student("Draco",40)
print(student1.name)
del student4.rollno #destroying an object
# student4.rollno = 54
# print(student4.rollno)

#ques 5
from unicodedata import name


class Employee:
    def __init__(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
#a
employee1.Salary = 70000
print(employee1.Salary) 
#b
del employee3 
# print(employee3.Name)

# ques 6
def permutations(string, space=""):
 
    if len(string) == 0:
        print(space)
 
    for i in range(len(string)):
 
        newSpace= space + string[i]
        newString = string[0:i] + string[i+1:]
 
        permutations(newString, newSpace)
 
s = input("word : ")
print(permutations(s))
