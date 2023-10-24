courses = ['MIL', 'CYBERSECURITY', 'DATA SCIENCE']

print(courses)

#Accessing an element in an array
print(courses[1])

#lopping in an array
for course in courses:
    print(course)

#adding an element in an array
courses.append("Android Development")
print(courses)

#remove an element from an array
courses.remove("MIL")
print(courses)