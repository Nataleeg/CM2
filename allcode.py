#Natalee, Davion, Marayah
#December 8, 2023
#Contact manager

def main():
    
    displayMeny()
    editContacts()
    displayContacts()
    
    
    menu = displayMenu()
    
    
def displayMenu():
    
    #Natalees code
    
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
#end of menu

#Natalee Granados
#November 27th 2023
#Modify Coffee Records

#This program allows the user to modify the quantity in a record in the coffee.txt file



    
def editContacts():
    
    found = False

    #Get the search value and the new quantity
    search = input('Enter a contact to search for: ')
    newInfo = int(input('Enter the new information: '))

    #Open the original coffee,txt file
    contactFile = open('contacts.txt', 'r')

    #Open the temporary file
    tempFile = open('temp.txt', 'w')
    
    #read the first records description field
    descr = contactFile.readline()

    #Read the rest of the file
    while descr != '':
        #Read the quantity field
        newInfo = int(contactFile.readline())
        
        #strip the\n from the s\descri[tion
        descr = descr.rstrip('\n')
        
        #write either this record to the temp file or the new record if this is the one that is to be modified

        if descr == search:
            #Write the modified record to the temp file
            tempFile.write(descr + '\n')
            tempFile.write(str(newInfo) + '\n')
            
            #set the found flag to true
            found = True

        else: 
# Write the original record to the temp file
            tempFile.write(descr + '\n')
            tempFile.write(str(newInfo) + '\n')
            
        #Read the next description
        descr = contactFile.readline()

    #close the coffe file and the temp file
    contactFile.close()
    tempFile.close()

    #delee the original coffe.txt file
    os.remove('contacts.txt')

    #Rename the temp file
    os.rename('temp.txt', 'contacts.txt')

    #If the search value was not found in the file display amessage

    if found:
        print('The file has been updated.')
    else: 
        print('That item was not found in the file.')
        #end of edit
        
#Natalee Granados
#November 30th, 2023
#Display

    displayContacts()
def displayContacts():
    
#open the coffee txt file
    contactFile = open('contacts.txt', 'r')

#Read the first record’s description field 
    descr = contactFile.readline()
#Read the rest of the file
    while descr != '':

#strip the \n from the description
        descr = descr.rstrip('\n')
        info = int(contactFile.readline())

#DIsplay the record
        print('Contact: ', descr)
        print('Contact info: ', info)

#Read the next description.
        descr = contactFile.readline()

#close the file
    contactFile.close()
#end of display

main()