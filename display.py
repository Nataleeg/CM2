#Natalee Granados
#November 30th, 2023
#Display

def main():
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

#call the main function 
main()
    
    
    