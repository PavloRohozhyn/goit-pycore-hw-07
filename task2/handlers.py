from validation import input_error, validation_for_add_function, \
    validation_for_change_function, validation_for_show_function
from utils import print_with_color 
from classes import AddressBook, Record
from errors import error_name_doesnt_exists


@input_error
def parse_input(user_input):
    """ PARSE input data """
    # get command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@validation_for_add_function
def add_contact(args, book: AddressBook) -> str | Exception:
    """ ADD contact """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@validation_for_change_function
def change_contact(args, book: AddressBook) -> str | Exception:
    """ CHANGE contact """
    name, old, new, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if old and new:
        record.edit_phone(old,new)
    return message


@validation_for_show_function
def show_phone(args, book: AddressBook) -> str | Exception:
    """ show PHONE """
    name, *_ = args
    record = book.find(name)
    # show PHONE
    if record:
        return str(record)
    return error_name_doesnt_exists(name)


def show_all(book: AddressBook):
    """ show ALL """
    if len(book) <= 0:
        print_with_color('Contact book is empty, use "add" command for add contact into book', 'yellow')
    for name, phone in book.data.items():
        print_with_color(f"{name}: {phone}", 'yellow')
    return True


@input_error
def add_birthday(args, book: AddressBook):
    """ add BIRTHDAY """
    name, bday, *_ = args
    record = book.find(name)
    if record:
        return record.add_birthday(bday)
    return error_name_doesnt_exists(name)


@input_error
def show_birthday(args, book: AddressBook):
    """ show BIRTHDAY """
    name, *_ = args
    record = book.find(name)
    if record.birthday:
        return str(record.birthday)
    else:
        return error_name_doesnt_exists(name)


def birthdays(book):
    """ show all birthdays that will take place during the next week."""
    if len(book) <= 0:
        print_with_color('Contact book is empty, use "add" command for add contact into book', 'yellow')
    # get all data about birthday
    pool_of_bday = book.get_upcoming_birthdays()
    if pool_of_bday:
        for item in pool_of_bday:
            print(f"Name: {item.name}, Congradultion day: {item.birthday}")
    else:
        return 'Unfortunately, there is no one to congratulate'
