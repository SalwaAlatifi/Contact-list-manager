#Contact list manager
import sys
contactList = []

def addNewContact():
    name = input("Enter name: ")
    phone = int(input("Enter phone number: "))
    contactList.append((name,phone))
    print("Contact saved!")

def viewAllContacts():
    for name, phone in contactList:
         print(f'Name: {name:>5} Phone Number: {phone:>4}')
        
def searchContactByName(Name):
    tem = ()
    for name, phone in contactList:
        if Name == name:
             tem = name, phone
             break
    
    if tem != None:
        Na , Ph = tem
        print(f'Name: {Na:>5} Phone Number: {Ph:>4}')
    else:
        print("The name is not exist in the contact manager")

def quit():
    sys.exit(0)
    

def menu():
     print("""
        1. Add a new contact
        2. View all contacts
        3. Search for a contact by name
        4. Quit
        """) 
     choice = int(input("Enter your choice: "))
     return choice


while(True):
    choice = menu()
    if choice == 1:
        addNewContact()
    elif choice == 2:
        viewAllContacts()
    elif choice == 3:
        searchContactByName(input("Enter the contact name: ").lower())
    elif choice == 4:
        quit()
    else:
        print("Inviald input try agine!")