# ques 1
string = input("Enter a string :")
word = input("Enter a word : ")
b = bool(string.find(word))
number = string.count(word)
print(number)
a = word.count(" ")
if a == 0 and b == True:  #counting number of occurences of each character when a single word is entered 
  for j in range(0, len(word)):
    print("no. of occurances of", word[j] , "is", string.count(word[j]))

#  ques 2
day = int(input("Day :"))
month = int(input("Month : "))
year = int(input("Year : "))
if 1<=month<12:
    month +=1
else:
 month = 12
if 1<=day<31:
    day += 1
else:
    day = 31
print("Next date is : ", day,"/", month,"/",year)

# ques 3
list = []
num =  int(input("Enter number of elements in the list : "))
for i in range(1,num+1):
  ele  = int(input("Enter number : "))
  list.append(ele)
list1 = []
for i in list:
  res = (i , i**2)
  list1.append(res)
print(list1)

# ques 4
grade = int(input("Enter your grade : "))
letter = ["A+", "A", "B+", "B", "C+", "C", "D"]
perf = ["Outstanding", "Excellent", "Very Good", "Good", "Average", "Below Average", "Poor"]
if 4<=grade<= 10:
  print("Your Grade is", letter[10 - grade], "and", perf[10 - grade],"Perforamnce" )
else:
  print("Error: input grade is out of range")

# ques 5
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
    print("")

# ques 6
from traceback import print_tb


d = {}
num = int(input("Enter number of sudents : "))
for i in range(1, num+1):
  Y = input("Enter name of student : ") #values
  N = int(input("Enter student's SID : ")) #keys
  d[N] = Y
print(d) #a
print(dict(sorted(d.items(), key=lambda item: item[1])))  #b #sorting using values = names
sorted(d.keys())
print(dict(sorted(d.items())))    #c #sorting using keys = sid
fname = int((input("Enter SID for finding details of student : "))) #d
print("Name of the student with SID ", fname, "is", d[fname])


#ques 7
num = int(input("Enter number of terms: "))
if num<0 :
  print("Number should be positive")
else:
  def Fibonacci(n):
    if n == 0:
     return 0
    if n ==1:
      return 1
    else:
      return Fibonacci(n-1)+Fibonacci(n-2)
sum = 0
for i in  range(0,num):
  print(Fibonacci(i),end = " ")
  sum = sum + Fibonacci(i)
print("\n","Average is : ", sum/num)

# ques 8
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
Seta = (Set1 | Set2) - (Set1 & Set2) #a
print(Seta)
Setb = (Set1 | Set2 | Set3) - ((Set1 & Set2) | (Set2 & Set3) | (Set3 & Set1)) #b
print(Setb)
Setc = ((Set1 & Set2) | (Set2 & Set3) | (Set3 & Set1)) - (Set1 & Set2 & Set3) #c
print(Setc)
Setn = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Setd = Setn - Set1 #d
print(Setd)
Sete = (Setn - Set1) & (Setn - Set2) & (Setn - Set3) #e
print(Sete)