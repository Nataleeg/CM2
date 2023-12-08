#Davion Brown
#Search Contacts
#Nov. 30, 2023

def main():
    #Creat a bool variable to use as a flag
    found = False
    
    #Tell user to enter a name or number to search for a contact
    search = input('Enter the name here: ')
    
    #Open the contact.txt file
    contact_file = open('contact.txt', 'r')
    
    #Get the name in contact.txt_file
    name = contact_file.readline()
    
    while name != '':
        #read the number
        number = contact_file.readline()
        
        #strip the \n from the name
        name = name.rstrip('\n')
        
        #Determine whether this contact matches
        #The search value
        if name == search:
            #Display the record
            print('Name:', name)
            print('Number:', number)
            print()
            #Set the found flag to true
            found = True
        #read the next description
        name = contact_file.readline()
            
    #Close the contact file
    contact_file.close()
    
    #if the contact was not found in the file
    #display a message
    if not found:
        print('This contact is not in your list')
#Call the main
main()

# >>> %Run search_Contacts.py
# Enter the name here: Jayden
# This contact is not in your list
# >>>

