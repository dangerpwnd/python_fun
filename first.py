# imports
import datetime

# variables
mynow = datetime.datetime.now()

# simple data types
# int
x = 10
# str
y = '10'
# float
z = 12.5

# complex data types
# list
# lists are indexed
student_grades = [9.1, 8.8, 7.9]
list(range(1,10,2))
# dictionary
student_grades = {"Mary": 9.1, "Jim": 8.8, "John": 7.5}
# tuple
# tuple immutable, list mutable
# student_grades = (6, 7.8, 9)

sum1 = x + x
sum2 = y + y

# print functions
print("The date and time is:", mynow)
print(sum1, sum2)
print(type(x),type(y))
print("Find attributes using dir()")
#print(dir(str))
print("List of builtin functions")
#print(dir(__builtins__))
# help functions
#help(str.upper)

# average function
mysum = sum(student_grades.values())
print(mysum)
itemlen = len(student_grades.values())
mean = mysum / itemlen
print(mean)

max_score = max(student_grades)
print(max_score)

monday_temperatures = [99.1, 92.4, 76.8]
monday_temperatures.append(85.1)
print(monday_temperatures)
print(monday_temperatures.index(92.4))
monday_temperatures.__getitem__(2)
#or
print(monday_temperatures[2])
#print last index
print(monday_temperatures[-1])

def mean2(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean
print(mean2(monday_temperatures))
print(type(mean2))
def sq(num):
    s= num*num
    return s
print(sq(4))

name = input("Enter your first name: ")
surname = input("Enter your last name: ")
message = "Hello %s %s" % (name, surname)
print(message)
message = f"Welcome {name} {surname}!"
print(message)