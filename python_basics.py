# variables
School = 'Minneapolis College'
gpa = 3.8
number_of_students = 30

# if elif else statements 
if gpa == 4.0:
    print("Thats awesome!")
elif gpa > 3:
    print("Keep up the good work!")

else: 
    print("Continue to work hard!")


# lists and in operator

Courses = [ 'python', 'math', 'science', 'history']

if 'python' in Courses:
    print(' Python is one of the courses!')

# strings

Class_name = 'Software Development'
print(Class_name.upper())
print(Class_name.split())
print(Class_name.split('o'))
print(len(Class_name))

if 'Development' in Class_name:
    print('yes')

Courses.sort()            # sort in place
print(Courses)

Courses.reverse     # reverse in place
print(Courses)

#add to list
Courses.append('fitness')
print(Courses)

# looping

for i in range(5):
    print(i)

# loops - for loops over sequences

for s in Courses:
    print(s.upper())

for the_class in School:
    print(the_class * 3)

data = [0] * 10
print(data)
more_data = [None] * 10
print(more_data)

# While Loops

name = input(" Enter your name. ")
while len(name) == 0:
   print( " You must enter a character. ")
#name = input("ENter you name. ")    

#while not len(name) == 0 :
    #print( "Thanks you " + name)


# True, False and None

Population = 100

print(Population > 1000)
print(Population < 50)




#Dictionaires

Student_ID = { 123: "Mark", 333: "Sally", 444: "Joe" }
for  y in Student_ID:
    print(y)

for x in Student_ID:
    print(Student_ID[x])

print(Student_ID[123])

for v, w in Student_ID.items():

    print(v, w)
    print(f' The Student ID is {v}, and the student name is {w} ')

 


# Slicing

Courses = [ 'python', 'math', 'science', 'history', 'art']
last_two_periods = Courses[1:3]
print(last_two_periods)
last_class = Courses[-1]
print(last_class)



# File IO
with open ('lab_1.txt') as f:
#opened = open('lab_txt') as f:
    data = f.read()
    print(data)

with open('lab_1.txt') as f:
    to_read = f.read()
    print(to_read)

with open('lab_1.txt', 'a') as f:
     f.write("this is lab 1\n")


# Functions

def ask_name():
    
    your_name = input(" What is your name ")

    return your_name




# Python warm up

your_name = input(" What is your name ")
print(" Hello " + your_name)

print(" You have " + str(len(your_name)) + " characters in your name")
birth_month = input( " What is your birth month ")

if birth_month.lower() == "august":
    print(" You should be greatfull for another year!")

else: 
    print( " It is not your birth month")

current_classes = input( " What classes are you taking this semester,? Seperate by comma. " )
List_of_classes = current_classes.split(',')

for i in List_of_classes:
    print(i.strip().title())














