#1
#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

list_of_numbers = []
numbers = input("Enter some numbers to add: ")
sumOf = 0
single_number = numbers.split()


for num in single_number:
    list_of_numbers.append(int(num))

for add in list_of_numbers:
    sumOf = sumOf + add

print(sumOf)

#2
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

favourite_books = ["Mo Dao Zu Shi", "Great Expectations", "Diary of a wimpy kid", "The Alchemist", "Eleanor and Park", "Scum Villian System"]

for book in favourite_books:
    print(book)

#3
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
    
person = {"name": "", "age": "" , "favourite colour": ""}
print(person)

name = input("Enter your name:")

age = input("Enter your age:")

colour = input("Enter your favourite colour:")

person["name"] = name
person["age"] = age
person["favourite colour"] = colour

print(person)