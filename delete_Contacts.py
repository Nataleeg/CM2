#Davion Brown
#Delete Contacts 
#Nov. 30, 2023

import os

def main():
    #Creat bool variable to use as a flag
    found = False
    
    #get the coffee to delete
    search = input('Which contact do you want to delete? ')
    
    #Open the original coffee.txt file
    contact_file = open('contact.txt', 'r')
    
    #Open the temporary file
    temp_file = open('temp.txt', 'w')
    
    #read the first record's description field
    name = contact_file.readline()
    
    #read the rest of the file
    while name != '':
        #read the number 
        number = contact_file.readline()
        
        #strip the \n from the description
        name = name.rstrip('\n')
        
        #If this is not the record to delete, then
        #write it to the tmeporary file
        if name != search:
            #Write the record to the temp file
            temp_file.write(name + '\n')
            temp_file.write(number)
        else:
            #Set the found flag to true
            found = True
            
        #Read the next description
        name = contact_file.readline()
        
    #Close the coffee file and the temporary file
    contact_file.close()
    temp_file.close()
    
    #Delete the original coffee.txt file
    os.remove('contact.txt')
    
    #Rename the temporary file
    os.rename('temp.txt', 'contact.txt')
    
    #If the search value was not found in the file
    #Display a message
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
    
#Call the main
main()

# >>> %Run delete_Contacts.py
# Which contact do you want to delete? Ethan
# That item was not found in the file.
# >>>

