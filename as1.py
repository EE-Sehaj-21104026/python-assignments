# program for finding average  ques1
x= input("Enter first number: ")
y= input("Enter second number: ")
z= input("Enter third number: ")
avg = (int(x)+int(y)+int(z))/3
print("The average of three numbers is: ", avg) 

# program to comput income tax ques2
x = float(input("Enter your Gross income: "))
y= int(input("Enter number of dependents: "))
a = (x-10000-(3000*y))
b = a*0.2
print("income Tax is: ", b)

#program to store data in a list ques3
x  =  [ 21104026, "Rabia", "F", "Electrical Engineering", 10]
print(x) 

# sorting lists ques4
x= [67, 45, 89, 78, 50]
x.sort()
print(x) 

# deleting elements of a list ques5
x = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
x.pop(3)
print(x)

#ques 5b 
x = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
del x[3:5]
x.insert(3, "Purple")
print(x)
