contact = {}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1.Add new Contact \n 2.View Contact List \n 3.Search Contact \n 4.Update Contact \n 5.Delete Contact \n 6.Exit \n1"))
    if choice == 1:
        name = input("Enter the name: ")
        number = input("Enter the mobile number")
        contact[name] = number 
    elif choice == 2:
        if not contact:
            print("empty contact")
        else:
            display_contact()
    elif choice == 3:
        search_name = input("Enter the contact name")
        if search_name in contact:
            print(search_name,"contact number is ",contact[search_name])
        else:
            print("Name is not found in contact ")
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited")
        if edit_contact in contact:
            number=input("Enter the mobile number")
            contact[edit_contact]=number
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want delete or not?")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact")
    else:
        break
     