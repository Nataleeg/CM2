#Natalee Granados
#November 30th, 2023
#Menu

def main():
    
def displayMenu():
    
    print("What do you want to do with your contact lists.")
    print("Please select a command from the list")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")
        
    if choice == 1:
        addContact()
    elif choice == 2:
        searchContact()
    elif choice == 3:
        editContact()
    elif choice == 4:
        deleteContact()
    elif choice == 5:
        displayContacts()
    else:
        print()
    
    
    return choice

main()