#Check a leap year (Any year that is evenly divisible by 4)
year = int(input("Enter year to be tested: "))
if(year % 4 == 0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")

#Checks vowels and consonants
letter = input("Enter a letter A-Z: ")
if letter.lower() in ('a', 'e', 'i', 'o'):
    print("It is a vowel letter")
elif letter.upper() in ('A', 'E', 'I', 'O'):
    print("It is a vowel letter")
else:
    print("It is a consonant letter")