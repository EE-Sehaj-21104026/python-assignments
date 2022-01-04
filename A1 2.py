# program to comput income tax
x = float(input("Enter your Gross income: "))
y= int(input("Enter number of dependents: "))
a = (x-10000-(3000*y))
b = a*0.2
print("income Tax is: ", b)