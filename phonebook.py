import re

contacts = {}


def list_of_options():
    print("1) list - lists all saved contacts in alphabetical order")
    print("2)show - finds a contact by name")
    print("3)find - searches for a contact by number")
    print("4)add - saves a new contact entry into the phone book")
    print("5)edit - modifies an existing contact")
    print("6) delete - removes a contact from the phone book")
    print("7)help - lists all valid commands")
    print("---------------------------")


def add_contact(name, number):
    if name in contacts:
        if number in contacts[name]:
            print(f"Number {number} already available for contact '{name}'.")
        else:
            contacts[name].append(number)
            print(f"Successfully added number {number} for contact '{name}'.")
    else:
        contacts[name] = [number]
        print(f"Successfully added contact '{name}'!")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def list_contacts():
    if contacts:
        for name, numbers in contacts.items():
            print(name)
            for number in numbers:
                print(number)
            print()
    else:
        print("No records found, the phone book is empty!")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def show_contact():
    name = input("Enter the name you are looking for: ").strip()
    if name in contacts:
        print(name)
        for number in contacts[name]:
            print(number)
    else:
        print("Sorry, nothing found!")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def find_contact():
    number = input("Enter a number to see to whom it belongs: ").strip()
    found = False
    for name, numbers in contacts.items():
        if number in numbers:
            print(name)
            print(number)
            found = True
    if not found:
        print("Number not found in the phone book.")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def edit_contact():
    name = input("Enter name of the contact you would like to modify: ").strip()

    if name in contacts:
        print(f"Current number(s) for {name}:")
        for number in contacts[name]:
            print(number)

        edit_option = input(
            "Would you like to add a new number or delete an existing number for this contact? [add/delete/cancel]: ").strip().lower()

        if edit_option == "add":
            new_number = input("Enter new number: ").strip()
            contacts[name].append(new_number)
            print(f"Number {new_number} was successfully added, record updated!")
        elif edit_option == "delete":
            number_to_delete = input("Enter the number you want to delete: ").strip()
            if number_to_delete in contacts[name]:
                contacts[name].remove(number_to_delete)
                print(f"Number {number_to_delete} was removed from the record for '{name}'")
            else:
                print("Number does not exist!")
        elif edit_option == "cancel":
            print("Contact was not modified!")
        else:
            print(
                "Invalid option! Use 'add' to save a new number, 'delete' to remove an existing number, or 'cancel' "
                "to go back.")
    else:
        print("Sorry, name not found!")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def delete_contact():
    name = input("Enter name of the contact to be deleted: ").strip()

    if name in contacts:
        confirmation = input(f"Contact '{name}' will be deleted. \n Are you sure you want to delete {name} from your "
                             f"contact list? [Y/N]: ").strip().lower()

        if confirmation == "y":
            del contacts[name]
            print("Contact was deleted successfully!")
        elif confirmation != "n":
            print("Invalid option! Delete contact? [Y/N]:")
    else:
        print("Sorry, name not found!")

    print("\nChoose a command or 'exit' to quit. For a list of valid commands use 'help':")


def main():
    print("WELCOME TO YOUR PHONE BOOK")
    print("===========================")
    print("Choose a command or 'exit' to quit:")
    list_of_options()

    options = input("> ").strip()

    while options != "exit":
        if options == "1":
            list_contacts()
        elif options == "2":
            show_contact()
        elif options == "3":
            find_contact()
        elif options == "4":
            add_contact()
        elif options == "5":
            edit_contact()
        elif options == "6":
            delete_contact()
        elif options == "7":
            list_of_options()
        else:
            print("Invalid command!")

        options = input("\n> ").strip()

    print("'Phone Book' terminated.")
