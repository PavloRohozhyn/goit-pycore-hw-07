""" import modules """
from utils import print_with_color, print_banner
from handlers import parse_input, add_contact, change_contact, show_all, show_phone, \
    add_birthday, show_birthday, birthdays
from classes import AddressBook, Record


# Main
def main():
    """ bot commands hendler """
    book = AddressBook()
    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # close, exit
        if  command in ["close", "exit"]:
            print_with_color("Good bye!", 'yellow')
            break

        # hello
        elif command in ["hello"]:
            print_with_color("How can I help you?", 'yellow')

        # add
        elif command in ["add"]:
            print_with_color(add_contact(args, book), 'yellow')

        # change
        elif command in ['change']:
            print_with_color(change_contact(args, book), 'yellow')

        # phone
        elif command in ['phone']:
            print_with_color(show_phone(args, book), 'yellow')

        # all
        elif command in ['all']:
            show_all(book)

        # add birthday
        elif command == "add-birthday":
            print_with_color(add_birthday(args, book), 'yellow')

        # show birthday
        elif command == "show-birthday":
            print_with_color(show_birthday(args, book), 'yellow')

        # birthday
        elif command == "birthdays":
            birthdays(book)

        # something else
        else:
            print_with_color("Invalid command.", 'yellow')


if __name__ == "__main__":
    print_banner()
    print("Welcome to the assistant bot!\n\n")
    print("List of commands")
    print_with_color("1.FGBS hello BESR say hello to the assistant")
    print_with_color("2.FGBS add [contact_name] [phone_number] BESR adds contact name and phone number to memory")
    print_with_color("3.FGBS change [contact_name] [old_phone_number] [new_phone_number] BESR edits the contact's phone number")
    print_with_color("4.FGBS phone [contact_name] BESR displays the contact's phone number")
    print_with_color("5.FGBS all BESR show contacts phone book")
    print_with_color("6.FGBS close BESR or FGBS exit BESR exit from the assistant")
    print_with_color("7.FGBS add-birthday [contact_name] [day_of_birthday] BESR add birthday of contact name")
    print_with_color("8.FGBS show-birthday [contact_name] BESR display day of birth")
    print_with_color("9.FGBS birthdays BESR show birthdays that will happen in the next week\n\n")
    # GO!
    main()
