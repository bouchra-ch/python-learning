#x = "WWWoooorrrldd"
#print (x[1:])

'''
def cleanword(word):
    if len(word) == 1:
        return word
    print(f"print start fuction {word}")
    if word[0] == word[1]:
        print(f"print before condition {word}")
        return cleanword(word[1:])
    print(f"print before return {word}")
    return word[0]+cleanword(word[1:])
print(cleanword("WWWoooorrrldd"))
'''

'''
def say_hello(name, age): return f"Hello, {name}! you have {age} years old."
hello = lambda name, age: f"Hello, {name}! you have {age} years old."

print(say_hello("ahmed", 36))
print(hello("ahmed", 36))

print(say_hello.__name__)
print(hello.__name__)

'''

'''
import os
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
'''

'''

print(myFile)

print(myFile.readline(2))
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
print(type(myFile.readlines()))
print(myFile.readlines(50))


myFile.close()
'''



contacts = []
def add_contact(name, age, email):
    contact = {
    "name": name,
    "age": age,
    "email": email
    }
    contacts.append(contact)

def show_contacts():
        for contact in contacts:
            for key, values in contact.items():
                print(f"{key}: {values}")
            print("---")

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            for key, value in contact.items():
                print(f"{key}: {value}")
            return
    print("contact not found")

while True:
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Quit")
    print("4. Search contact")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Please enter a valid number!")
            age = 0
        email = input("Email: ")
        add_contact(name, age, email)
        print("Contact added!")
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        break
    elif choice == "4":
        name = input("enter name to search: ")
        search_contact(name)



