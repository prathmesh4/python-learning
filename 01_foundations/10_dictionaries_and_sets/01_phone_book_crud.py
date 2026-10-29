contacts={}
def print_not_found():
    print("Contact not found!!")
    
while True:
    print("===========Phone Book============")
    print("1. Add a Contact")
    print("2. Search by name")
    print("3. Delete a Contact")
    print("4. Show all contacts")
    print("5. Exit")
    
    choice=input("Enter your choice: ").strip()
    if choice=="1":
        name=input("Enter a Name: ").strip()
        phone=input("Enter phone number: ").strip()
        
        contacts[name]=phone
        print("Contact saved!",name)
    elif choice =="2":
        name=input("Enter a name for search:").strip()
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print_not_found()
    elif choice=="3":
        name=input("Enter name for delete:").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact deleted! {name}")
        else:
            print_not_found()
    elif choice=="4":
        if not contacts:
            print("Phone book is empty!")
        else:
            print("All Contacts:")
            for name,phone in contacts.items():
                print(f"{name} : {phone}")
    elif choice=="5":
        print("Exitting phone book!!!")            
        break
    else:
        print("Invalid Choice! Please enter valid choice.")
        
"""Phone Book
Dictionary CRUD with a menu loop
Build a contact manager backed by a dictionary (name -> phone number). Offer a menu that loops until the user exits:
• Add a contact
• Search by name
• Delete a contact
• Show all contacts

Handle the "contact not found" case cleanly instead of crashing.

Example:

> add    Prathmesh 8857935193
> add    Pranav 9123456780
> search Prathmesh   -> Prathmesh: 8857935193
> delete Pranav   -> Deleted Pranav
> show           -> Prathmesh: 8857935193

Hint: use .get() so a missing name returns None instead of raising a KeyError.
"""        