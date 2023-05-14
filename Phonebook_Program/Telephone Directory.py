'''
Application name: Phonebook

Application Type: Telephone Directory

Data of work start: 24 Apr 2023

Work finished: 11 May 2023

Application description:
Phonebook is formed by a changable list of entries stored in the outter file. 
Each data entry represents a list of contacts with details for each individual contact such as:
- first name
- last name 
- age
- sex 
- telephone number 
- address  

 The application is PASSWORD protected and have the following utilities:  
	- Display all contacts and all of their relevant details  
	- Search by name (by entering one or more characters) displaying all contacts that 	fit the search  
	- Search by telephone number (by entering one or numbers) displaying all contacts the fit the search  
	- Add a new contact  
	- Remove a contact (using name and or telephone number)  
    - When exiting the contact list should be written back to the file or database  
'''



# ========================================================================================================

def password(names,surnames,ages,sexes,phones,addresses):
    print("\nThe program PHONEBOOK is Password-protected.")
    count=0
    while count<3:
        password=input("\nEnter the Password: ")
        
        if password!="123":
            count=count+1
            print(f"The password is Wrong! you have {3-count} attempts.")
            if count==3:
                print("You entered wrong password 3 times.\nAccess DENIED. Good-bye...\n")
                exit(0)
        if password=="123":
            print("\nAccess GRANTED!")
            readData(names,surnames,ages,sexes,phones,addresses)
            


# ========================================================================================================        

def main():
    
    names=[]
    surnames=[]
    ages=[]
    sexes=[]
    phones=[]
    addresses=[]
    
    password(names,surnames,ages,sexes,phones,addresses)

   

# ========================================================================================================

def readData(names,surnames,ages,sexes,phones,addresses):
    
    with open("Tel data.txt", "r") as myFile:
        for line in myFile:
            details=line.split(",") 

            names.append(details[0])
            surnames.append(details[1])  
            ages.append(details[2])
            sexes.append(details[3])
            phones.append(details[4])
            addresses.append(details[5].strip("\n"))
        print("All the data are propoerly transferred from the file to the computer memory")
        input("\nPress ENTER to open Main Menu >>>")
        menu(names,surnames,ages,sexes,phones,addresses)

# ========================================================================================================

def menu(names,surnames,ages,sexes,phones,addresses):
    while True:
        main="Main MENU"
        print(f"\n{main:>180}\n")
        selection=input("1 \t Display all contacts and all of their relevant details \n2\t Search by name (by entering one or more characters) displaying all contacts that fit the search\n3\t Search by telephone number (by entering one or more digits) displaying all contacts the fit the search \n4\t Add new contact(s)\n5\t Remove a contact (using name and or telephone number)\n6\t When exiting the contact list should be written back to the file or database\n\nPlease make your selection: ")
        if selection=="1":
        
            printer(names,surnames,ages,sexes,phones,addresses)
            input("\nPress ENTER to continue to Main Menu >>>")

        if selection=="2":
            searchByName(names, surnames,ages,sexes,phones,addresses)
            input("\nPress ENTER to continue to Main Menu >>>")

        if selection=="3":
            searchByNumber(names, surnames,ages,sexes,phones,addresses)
            input("\nPress ENTER to continue to Main Menu >>>")


        if selection=="4":

            addContact(names,surnames,ages,sexes,phones,addresses)
            input("\nPress ENTER to continue to Main Menu >>>")

        if selection=="5":
            
            removeContact(names, surnames, ages, sexes, phones, addresses)
            input("\nPress ENTER to continue to Main Menu >>>")

        if selection=="6":
            choice=input("Do you want to save the changes done? (y/n): ")
            if choice=="y" or choice=="Y":
                exportData(names,surnames,ages,sexes,phones,addresses)
            else:
                print("The changes were not saved")
            print("Thank you, Bye!\n")
            exit(0)

# ========================================================================================================

def printer(names,surnames,ages,sexes,phones,addresses):
    p="Selection1: The Full Content of the Phonebook"
    print(f"{p:>200}\n")
    print("#\tName\t  Surname\tAge\tGender\tPhone\t\tAddress ")
    for i in range(len(names)):
        print(f"{i+1}.\t{names[i]:<10}{surnames[i]:<10}\t{ages[i]}\t{sexes[i]}\t{phones[i]}\t{addresses[i]} ")

# ========================================================================================================

def searchByName(names, surnames,ages,sexes,phones,addresses):
    p="Selection 2: Search by Name and Surname"
    print(f"{p:>200}\n")
    found=bool(False)
    letters=input("\nIf NO letters entered - entire list will be presented. \nPlease make enter the letters for search: ")
    print("")
  
    index=0
    c1=0
    c2=0

    while index<(len(names)):
        if names[index].__contains__(letters.capitalize()) or names[index].__contains__(letters.lower()):
            print(f"{names[index]:<10}{surnames[index]:<10}\t{ages[index]}\t{sexes[index]}\t{phones[index]}\t{addresses[index]}")
            found=bool(True)   
            c1=c1+1
        elif surnames[index].__contains__(letters.capitalize()) or surnames[index].__contains__(letters.lower()):
            print(f"{names[index]:<10}{surnames[index]:<10}\t{ages[index]}\t{sexes[index]}\t{phones[index]}\t{addresses[index]}")
            found=bool(True)   
            c1=c1+1
        index=index+1
    print(f"\nTotally found {c1+c2} coincidences out of {index} entries")

    if found==bool(False):
        print("The Name is NOT found in the list")

# ========================================================================================================

def searchByNumber(names,surnames,ages,sexes,phones,addresses):
    p="Selection 3: Search by Phone Number"
    print(f"{p:>200}\n")
    found=bool(False)
    index=0
    c1=0
    c2=0
 
    digits=str(input("Enter One or More digits to find the phone number: "))
    while index in range (len(phones)):
        if phones[index].__contains__(digits):
           print(f"{names[index]:<10}{surnames[index]:<10}\t{ages[index]}\t{sexes[index]}\t{phones[index]}\t{addresses[index]}")
           found=bool(True) 
           c1=c1+1
        
        index=index+1
    
    print(f"Totally found {c1} coincidences out of {index} entries")

    if found==bool(False):
        print("The Number is NOT found in the list")

# ========================================================================================================

def addContact(names,surnames,ages,sexes,phones,addresses):
    
    p="Selection 4: Add New Contact(s)"
    print(f"{p:>200}\n")
    numberToAdd=int(input("Enter the Number of people to be added: "))
    count=0
    while count<numberToAdd:
        count=count+1
        name=input("Enter the Name: ")
        surname=input("Enter the Surname: ")
        age=input("Enter the Age: ")
        sex=input("Indicate gender m/f: ")
        phone=input("Enter the Phone number: ")
        address=input("Enter the Address: ")
        names.append(name)
        surnames.append(surname)  
        ages.append(age)
        sexes.append(sex)
        phones.append(phone)
        addresses.append(address)

        print("The changes were propoerly added to the list")

# ========================================================================================================
        
def removeContact(names, surnames, ages, sexes, phones, addresses):
    p="Selection 5: Delete a contact"
    print(f"{p:>200}\n")
    if (len(names))==0:
        print("The list is empty. There are no elements in the list to delete.")
    else:
        nameToRemove=input("Enter the name to be removed: ")
        if (nameToRemove in names):
            index=names.index(nameToRemove)
            print(f"\nName to be removed is #{index+1} in the list \n")
            print("#\tName\t  Surname\tAge\tGender\tPhone\t\tAddress ")
            print(f"{index+1}.\t{names[index]:<10}{surnames[index]:<10}\t{ages[index]}\t{sexes[index]}\t{phones[index]}\t{addresses[index]} \n")
            choice=input("do you want to DELETE the person and all its details from the list? (y/n): ")
            if choice=="y":
                del names[index]
                del surnames[index]
                del ages[index]
                del sexes[index]
                del phones[index]
                del addresses[index]
                print(f"'{nameToRemove}' was suceessfully deleted from the list with all the data afiliated")
            else:
                print("Deleting CANCELLED by the User")
        else:
            print(f"There is NO '{nameToRemove}' in the list! Deleting CANCELLED")

# ========================================================================================================

def exportData(names,surnames,ages,sexes,phones,addresses):

    with open("Tel data.txt","w") as file:
        for i in range (len(names)):
            file.write(f"{names[i]},{surnames[i]},{ages[i]},{sexes[i]},{phones[i]},{addresses[i]}\n")

        print("All the data are properly saved in the designated File")

# ========================================================================================================

if __name__=="__main__":
    main()
