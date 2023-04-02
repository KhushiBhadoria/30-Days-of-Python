'''Python Variable -> Variable is a container that stores value. As Pyhton is not "Statically Typed". So we don not need to declare
 variable before using them. A variable is created the moment we assign a value to it.
   '''
var='Python!!!'
print(var)# Python!!!

'''Rules for Declaring variable in python
1. A Python variable name must start with a letter or the underscore character.A Python variable name cannot start with a number.
2. A Python variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
3. Variable in Python names are case-sensitive (name, Name, and NAME are three different variables).
4. The reserved words(keywords) in Python cannot be used to name the variable in Python.
'''
python=1 #valid
_python=2 #valid
_python_=3 #valid
Python=4 #valid
Pyt_hon=6 #valid
#9python=7 #invalid

#Assign value to multiple variable
a=b=c=d=20
print(a,b,c,d) # 20 20 20 20

#Assigning different values to multiple variables
a,b,c,d=1,4.0,67,'Name'
print(a,b,c,d) # 1 4.0 67 Name

# Can we use same name for different type
#If we use the same name, the variable starts referring to a new value and type. 
a=2
a=89
print(a)# 89

