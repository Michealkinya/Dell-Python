
number = 100 #int
second = 56.78 #float
text = "Hello there" #str
ispythoninteresting = True #boolean

#Storing Multiple VAlues in a variable
cars = ["toyota", "Nissian", "Vitz"] #List
fruits = ["banana", "Oranges", "Mangoes"] #Tuple
countries = ["Kenya", "Ghana", "Algeria"] #Ser
details = {
    "Firstname" : "Mike",
    "Age" : 35,
    "Course" : "Web Development",
    "nationality" : "Kenyan"
} #nationality

print(second)
print(text)
print(cars)
print(countries)
print(details["Firstname"])
print(details["Age"])

#Determine the data type
print(type(text))
print(type(details))

#Typecasting - converting one data type to another
print(float(number))
print(int(second))
