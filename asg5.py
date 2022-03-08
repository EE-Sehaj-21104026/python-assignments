#ques 1
import tkinter as tk
from tkinter import *
scrn = Tk()
label_text=StringVar();
scrn.title("Gst Tax Finder")
scrn['bg']= "light blue"
scrn.geometry('400x400')
lbl1 = Label(scrn, text = "Original coast ", font = ("Sitka Subheading Semibold", 20), fg = "black", bg = "light blue")
entry1 = Entry(scrn, bg = "light grey", width = 10, font= ("helvetica",20), fg = "dark blue")
lbl1.place(x = 10, y = 0)
entry1.place(x = 200, y = 10)
lbl2 = Label(scrn, text = "Net Price ", font = ("Sitka Subheading Semibold", 20), fg = "black", bg = "light blue")
entry2 = Entry(scrn, bg = "light grey", width = 10, font= ("helvetica",20), fg = "dark blue")
lbl2.place(x = 20, y =60 )
entry2.place(x = 200, y = 65)
lbl3= Label(scrn, text = "GST Rate ", font = ("Sitka Subheading Semibold", 20), fg = "black", bg = "light blue")
result = Label(scrn, text ="", textvariable = label_text, fg ="Red", bg = "light blue", font = ("Calibri", 15,'bold'))
result.place(x=219, y = 210)
lbl3.place(x = 100, y = 200)
def gst():
    res = ((float(entry2.get()) -  float(entry1.get()))*100)/ float(entry1.get())
    # res = (float(entry1.get())*Gst_rate)/100
    label_text.set('%0.3f'%(res))
b = Button(scrn, text="Calculate" ,font = ("Sitka Subheading Semibold", 10), bg = "orange", fg = "blue", command=gst)
b.place(x = 150, y = 150)
scrn.mainloop()


#ques 2
import tkinter as tk
from tkinter import *
import calendar
def proCalendar():
    cal = Tk()
    cal.title("Calendar")
    cal.geometry('800x800')
    cal['bg']="#1f2833"
    year = int(year_entry.get())
    cal_contents = calendar.calendar(year)
    calyear = Label(cal, text = cal_contents, font = ("Consolas", 14), fg = "#66fcf1", bg = "#1f2833")
    calyear.place(x = 0, y = 0)
    cal.mainloop()
if __name__=='__main__':
    ncal = Tk()
    ncal.title("Calendar")
    ncal.geometry('400x400')
    ncal['bg']="#5CDB95"
    cal = Label(ncal, text="Calendar", font=("Bahnschrift SemiBold", 30, "bold"), fg= "#282828", bg = "#5CDB95")
    year = Label(ncal, text = "Enter year", bg = '#5CDB95', font=("Consolas", 20, 'bold'), fg = '#3500D3')
    year_entry =Entry(ncal, font =('Consolas', 19), width = 6, bg = '#E27D60')
    button = Button(ncal, text = 'Show Calendar', command = proCalendar, font = ("Consolas",17, 'bold' ), fg = '#05386B', bg = "#E7717D")
    Exit = Button(ncal, text = 'Exit', command= ncal.destroy, font = ("Consolas", 17, 'bold'),fg = '#EFE2BA', bg ='#F13C20')
    cal.place(x = 130 , y = 0)
    year.place(x= 10, y = 70)
    year_entry.place(x = 200, y = 75)
    button.place(x= 50, y = 150)
    Exit.place(x = 50, y = 240)
    ncal.mainloop()


#ques 3
import tkinter as tk
from tkinter import*
calc = Tk()
calc.geometry('350x350')
calc.title('Calculator')
calc.maxsize(width = 250, height = 320)
# calc.minsize('200x200')
ent = Entry(calc,  width = 15,borderwidth = 1,bg = '#f2ffff', font=("Franklin Gothic Demi",18), fg = "#000033", relief= SUNKEN)
calc['bg']= '#6f6f6f'
ent.grid(pady = 10,row=0,sticky ='w', padx =18 )
def delete():
    a = ent.get()
    ent.delete(first=len(a)-1,last='end')
def result():
    if ent.get()=="":
        pass 
    elif ent.get()[0]=='0':
        ent.delete(0, 'end')
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        resf()
        ent.insert('end', c_res)
def resf():
    ent.delete(0, 'end')
clear = Button(calc, text = "C",font = ("Candara Light", 11, 'bold'), width= 3,command= resf, bg = '#FF6600', fg = "white", relief = RAISED)
clear.grid(pady = 10,row=1,sticky ='w', padx =10)
delete = Button(calc, text ="del", command = delete,font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF6600', fg = "white", relief = RAISED)
delete.grid(pady = 10,row=1,sticky ='w', padx =65)
modulus = Button(calc, text = "%",command = lambda: ent.insert("end", "%"),font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF0033', fg = "white", relief = RAISED )
modulus.grid(pady = 10,row=1,sticky ='w', padx =120)
divide = Button(calc, text = "/",command = lambda: ent.insert("end", "/"),font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF0033', fg = "white", relief = RAISED)
divide.grid(pady = 10,row=1,sticky ='w', padx =175)
seven = Button(calc, text = "7",command = lambda: ent.insert("end", "7"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
seven.grid(pady = 10,row=2,sticky ='w', padx =10)
eight = Button(calc, text = "8",command = lambda: ent.insert("end", "8"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
eight.grid(pady = 10,row=2,sticky ='w', padx =65)
nine= Button(calc, text = "9",command = lambda: ent.insert("end", "9"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
nine.grid(pady = 10,row=2,sticky ='w', padx =120)
multiply = Button(calc, text = "*",command = lambda: ent.insert("end", "*"),font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF0033', fg = "white", relief = RAISED )
multiply.grid(pady = 10,row=2,sticky ='w', padx =175)
four= Button(calc, text = "4",command = lambda: ent.insert("end", "4"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
four.grid(pady = 10,row=3,sticky ='w', padx =10)
five= Button(calc, text = "5",command = lambda: ent.insert("end", "5"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
five.grid(pady = 10,row=3,sticky ='w', padx =65)
six= Button(calc, text = "6",command = lambda: ent.insert("end", "6"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
six.grid(pady = 10,row=3,sticky ='w', padx =120)
subtract = Button(calc, text = "-",command = lambda: ent.insert("end", "-"),font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF0033', fg = "white", relief = RAISED )
subtract.grid(pady = 10,row=3,sticky ='w', padx =175)
one= Button(calc, text = "1",command = lambda: ent.insert("end", "1"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
one.grid(pady = 10,row=4,sticky ='w', padx =10)
two= Button(calc, text = "2",command = lambda: ent.insert("end", "2"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
two.grid(pady = 10,row=4,sticky ='w', padx =65)
three= Button(calc, text = "3",command = lambda: ent.insert("end", "3"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
three.grid(pady = 10,row=4,sticky ='w', padx =120)
add = Button(calc, text = "+",command = lambda: ent.insert("end", "+"),font = ("Candara Light", 11, 'bold'), width= 3, bg = '#FF0033', fg = "white", relief = RAISED )
add.grid(pady = 10,row=4,sticky ='w', padx =175)
zero= Button(calc, text = "0",command = lambda: ent.insert("end", "0"),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "#cccccc", relief = RAISED)
zero.grid(pady = 10,row=5,sticky ='w', padx =10)
point= Button(calc, text = ".",command = lambda: ent.insert("end", "."),font = ("Candara Light", 12, 'bold'), width= 3, bg = '#262626', fg = "white", relief = RAISED)
point.grid(pady = 10,row=5,sticky ='w', padx =65)
equal= Button(calc, text = "=",command =result,font = ("Candara Light", 12, 'bold'), width= 6, bg = '#FF6600', fg = "white", relief = RAISED)
equal.grid(pady = 10,row=5,sticky ='w', padx =120)
calc.mainloop()

#ques 4
#using quick sort
n = int(input("Enter number of students: "))
mlist =[]
for i in range(0, n):
    a = int(input("Marks of student: "))
    mlist.append(a)
print("Entered marks list: ", mlist)
def sort(array, low, high):
    pivot =array[high]
    i = low -1
    for j in range(low, high):
        if array[j]<=pivot:
            i+=1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1],array[high])=(array[high], array[i+1])
    return i+1
def quicksort(array, low, high):
    if low<high:
        pi =sort(array, low, high)
        quicksort(array, low,pi-1)
        quicksort(array, pi+1, high)
quicksort(mlist,0,len(mlist)-1)
print("marks list sorted by quick sort")
print(mlist)

#using merge sort
def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

mergeSort(mlist)
print("marks list sorted by merge sort ")
print(mlist)

#ques 5
n = int(input("Number of entries: "))
mlist =[]
for i in range(0, n):
    a = int(input("Entry number "+ str(i)+": "))
    mlist.append(a)
print("Input array: ",mlist)
#a sorting the array
def sort(array, low, high):
    pivot =array[high]
    i = low -1
    for j in range(low, high):
        if array[j]<=pivot:
            i+=1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1],array[high])=(array[high], array[i+1])
    return i+1
def quicksort(array, low, high):
    if low<high:
        pi =sort(array, low, high)
        quicksort(array, low,pi-1)
        quicksort(array, pi+1, high)
quicksort(mlist,0,len(mlist)-1)
print("Sorted array")
print(mlist)

#b
num = int(input("Enter number to be searched : ")) 
def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    mid =0
    while low<= high:
        mid = (high+low)//2
        if arr[mid]<x:
            low = mid +1
        elif arr[mid] >x:
            high = mid-1
        else:
            return mid
            return -1
result = binary_search(mlist, num)
if result != -1:
    print("Element is present in the input array")
else:
    print("Error: Element is not present in the input array")

#c
ocr = mlist.count(int(num))
print("Number of occurances of element "+str(num)+" is : "+str(ocr))








