# # var1="value"
# # # print(var1[-2])
# # # print(var1[1: ])
# # # print(len(var1))
# # # print(type(var1))
# # # var2=10
# # # print(type(var2))
# # # var3=True
# # # print(type(var3))
# # # var4=2.78
# # # print(type(var4))
# # # comp=complex(8+4j)
# # # print(type(comp))
# # # print(var1,var2,var3,var4,comp)
# # str1="hello"
# # str1="y"+str1[1:]
# # print(str1)
# # str2=str1[0:2]+"mm"+str1[4:]
# # print(str2)

# # if num1 %2 ==0 and nim1 %3 == 0:
# #      print('not prime')
# # elif num1 % num1 == 1 and num1 % 1 == num1:
# #     print('prime')

# # num1=int(input(Entar a number))
# # if num1==1:

# # try:
# #     summation += int(n)
# #     list3[list3.index(n)] = float(n)

# #   except valeue Error:
# #       print('nota number')
# #       list3.remove(n)
# #       print(n)

# # print(list3)
# # maxi=max(list3)
# # mini=min(list3)
# # print('sum=', summation)

# # studant={'name':'','age':0, 'country':'', 'city':'', 'job':'', 'skills':[],'prant':{'father':'','mother':''}}

# # print(student) 
# # for i in student
# # if type(student[i]) == int
# #        studnet[i] = input ('enter the ' + i + ':'))

# # elif type(student[i]) == list:
# # times = int(input('how many skills do you hav'))


    
# # esraa=input('Please enter a word')

# # for n in range  (0,len(esraa)):
# #   if(esraa[n]=='l'or esraa[n]=='u'or esraa[n]=='L' or esraa[n]=='U'):
# #      print('*')
# #   else:
# #     print (esraa[n])
# # v1= int(input('please enter a number'))
# # v2= int(input('please enter another number'))
# # v3='Esraa'

# # def myfunction(v1,v2):
# #   return v1+v2,v3

# # print ('the sum =', myfunction(v1,v2))

# #
# # names = ['Alice', 'David', 'Carolina', 9]
# # # >>> lists can take diffrent data types
# # test = ['test']
# # names.append('mohammad')
# # #1 append: add new value to the list at the end
# # # print(names)
# # #2 insert : add new value to the list at a specific chossen index number.
# # names.insert(1, 'khaled')
# # print(names)

# #3 extend : add new list to the excisting list at the end of the list
# # list1 = [1, 2, 3, 4, 5,1,1]
# # list2 = [6, 7, 8, 9]
# # list2.extend(list1)
# # list2=list2+list1
# # print(list2)

# #4 sum: is used to get the summation of a list
# # can't do summation for a list with diffrent data types inside
# # print(sum(list1))

# # print(list1.count(1))
# #5 count: to get the number of times an item is found in a list

# # print(len(list1))
# #6 to get the number of items in a list

# #7 index: to get the index of the first apperance of a value in a given list
# # print(list1.index(4))

# # >>>> print max and min values of list2>>>>
# # maxvalue = 0
# # minvalue = 6
# # for i in list2:
# #   if i > maxvalue:
# #     maxvalue = i

# # print(maxvalue)
# # for n in list2:
# #   if n < minvalue:
# #     minvalue = n

# # print(minvalue)

# #8 max&min : to get the maximum number and minimum number of a list
# # print(max(list2))
# # print(min(list2))

# #9 pop: to remove an item based on its index from a given list
# # print(list1.pop(1))
# # print(list1)

# # # to remove the last item of a list
# # list1.pop()
# # print(list1)

# # # to print the last value of a given list
# # print(list1.pop())

# # #10 remove: remove an item form a given list
# # list1.remove(1)
# # print(list1)

# # #reverse: used to reverse the items of a list
# # list1.reverse()
# # print(list1)

# # list1.sort(reverse=True)
# # print (list1)

# #Homework>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # list3 = ['1', 2.5, 3, 'e', 5, 6.001, 7, 0.02, 9, 6]
# # summation = 0
# # for n in  list3 :
# #   try:
# #      summation += float(n)
# #      list3[list3.index(n)]=float(n)
# #   except ValueError:
# #      print(n,'not a number')
# #      list3.remove(n)
# # print(list3)
# # # maxi=max(list3)
# # # mini=min(list3)
# # print('Sum=', summation)
# # print('Avg=', summation / 10)
# # print( 'Maximum number is ',max(list3))
# # print( 'Minimum number is',min(list3))

# # print('Index of max. value', list3.index(max(list3)))
# # print('Index of min. value', list3.index(min(list3)))
# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # students = []

# # reinter = True
# # while reinter:
# #   student = {}
# #   insertTime = int(input('how many key do you want to add?'))
# #   for i in range(insertTime):
# #     deckey = input('enter the key')
# #     decvaluetype = int(
# #       input(
# #         'enter the type of the value where 1 foor str 2 for int 3 for list and 4 for dectionary'
# #       ))
# #     if decvaluetype == 1:
# #       decvalue = input('enter the value:')
# #     elif decvaluetype == 2:
# #       decvalue = int(input('enter the value:'))
# #     elif decvaluetype == 3:
# #       decvalue = []
# #       times = int(input('how many' + deckey + 'o you have?'))
# #       for j in range(times):
# #         decvalue.append(input('enter the value' + deckey + ':'))
# #     elif decvaluetype == 4:
# #       decvalue = {}
# #       times = int(input('how many' + deckey + 'do you have'))
# #       for m in range(times):
# #         keynew = input('enter the key:')
# #         newvalue = input('enter the value')
# #         decvalue[keynew] = newvalue
# #     student[deckey] = decvalue
# #     anyvar = student
# #     students.append(student)
# #     continue0rnot = input('do you want to add another student?')
# #     if continue0rnot == 'no':
# #       reinter = False

# # print(students)
          
# # class client:

# #   def_init_(self, nameopj ='deafult', phoneopj=123456789, Emaiopj=, "mohd@gmail.com", puropj=5)
# #   self.name = nameopj
# #   self.phone = phoneopj 
# #   self.email = Emailopj
# #   self.purchies = propj

# #   def_ str_(self):
# #   print('hello')
# #   return f'name is {self.name} and phone is {self phone} and mail is{self. email} and purchie'


# # print ('hi to my program ')
# # name = input('enter your name:') 
# # age = int(input('enter your age:'))
# # grade = int(input ('enter your grade:'))
# # city = input('enter your city:')
# # speacialise = input ('enter your speacialise')
# # # pass the user input to the class
# # student1= student(name,age,grade, city,speacialise)
# # print('information added successfully')
# # #added new course to the student course method 
# # print("add new course ")
# # course= input (enter the course name:')
# # print(student1.addcorse(course))
# # print(student1)

# class Student:
#     def __init__(self,name='default',grade=1,age=18,city='riyadh',specalies='computer',password='123456'):
#       self.name=name
#       self.grade=grade
#       self.age=age
#       self.city=city
#       self.specalies=specalies
#       self.password=password

#     def __str__(self):
#         return f'name is {self.name} and age is {self.age} and grade is {self.grade}and city is {self.city}and specalies is {self.specalies}'
        
#     def talk(self):
#         return f'hello my name is {self.name}'
#     def addcorse(self,newcourse):
#         print(self.talk())
#         return f'hello {self.name} you have added {newcourse} to your courses'

# Students=[]
# while True:
#     print('Welcome to my program')
#     print('1-login')
#     print('2-register')
#     print('3-exit')
#     userchoice=int(input('plesae enter your choice:'))
#     if userchoice==1:
#         print('Welcome to the login page')
#         while True :
#             username=input('please enter your username:')
#             password=input('please enter your password:')
#             for i in range (len(Students)):
#               if Students[i].name ==username and Students[i].password==password:
#                 print('youre logged in succesfully!')
#                 print(Students)
#                 break
#               else:
#                   print('wrong username or password!')
#           #  another solution. 
#           # for student in Students:
#           # if student.name==username and student.password==password
#           # print('you logged in succesfully1') 
    
#     elif userchoice==2:
#         name=input('enter your name:')
#         age=int(input('enter your age:'))
#         grade=int(input('enter your grade:'))
#         city=input('enter your city:')
#         specalies=input('enter your specialies:')
#         password= input('enter your password:')
#         student1=Student(name,age,grade,city,specalies,password)
#         Students.append(student1)
#         print('information added succesfully!')
#         print(student1)
#     elif userchoice==3:
#         break
# print('information added succesfully!')
# pecalies=input('enter your specialies:') 
# print(student1)



# class father:

#      def_init_(self, name='sa'
#        return f'name is {self.name} and age is {self.age}'


# class son(father)



# class square:

#      def __init__(self) :
#         self 
#      def _str_(self):

#  class square:

# class Father:
#   def __init__(self,name,age,hairColor):
#     self.father=name
#     self.fatherage=age
#     self.haircolor=hairColor

#     def talk(self):
#       return f'my name is {self.father}'
    
# class Mother:
#     def __init__(self,name,age,hairColor):
#       self.mother=name
#       self.motherage=age
#       self.haircolor=hairColor
#     def talk(self):
#      return f'my name is {self.mother}'   
 
# class Party:
#    def __str__(self,location):
#     self.location=location

#    def __str__(self):
#      return self.location
   
# class Son(Mother,Father,Party):
#  Data class : a calss that contains only data (fields,att) and no methods. 
# 

from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# def name():
#     print("Hi from tkinter")
# ttk.Label(frm, text="Hello world!").grid(column=2, row=0)
# ttk.Button(frm, text="Quit", command=name()).grid(column=1, row=0)
# root.mainloop()

window= Tk()
window.title=("welcome to likegeeks app")
window.geometry('350x200')
lbl=Label (window,text="Hello")
lbl.grid(column=0,row=0)
count1=0

def clicked():
    global count1
    count1 +=1
    print(count1)
    lbl.configure(text=f'count = {count1}')

def printinput():
    inp=inputtxt.get(1.0,'end-1c')
    lbl.config(text= "provided Input:"+inp)
          
    
# input1= Entry(window,width=10)
inputtxt=Text(window,height=5,width=20) 
inputtxt.pack() 
btn = Button(window,text='Click Me', command=clicked)
btn.grid(column=1,row=0)
window.mainloop()

      


















      
       

          