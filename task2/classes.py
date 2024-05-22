""" import UserDict """
from collections import UserDict
import re
import sys
from datetime import datetime, timedelta


class Field:
    """ field element """

    def __init__(self, value):
        self.value = value

    # sting representation
    def __str__(self):
        return str(self.value)


class Name(Field):
    """ contact name """

    def __init__(self, value):
        super().__init__(value)
        self.value = value


    def __iter__(self):
        """Iterate over attributes"""
        yield self.value


class Phone(Field):
    """ contact phones """

    def __init__(self, value):
        super().__init__(value)
        if self.validation(value):
            self.value = value
        else:
            raise ValueError('')


    def validation(self, phone):
        """ phone validation, only 10 numbers """
        return re.match(r'^[0-9]{10}$', phone)


class Birthday(Field):
    """ birthday field """

    def __init__(self, value: str):
        super().__init__(value)
        if self.validation(value):
            self.value = datetime.strptime(value, '%d.%m.%Y')
        else:
            raise ValueError ('Invalid date format. Use DD.MM.YYYY')


    def validation(self, value):
        """ validation datetime """
        return datetime.strptime(value, '%d.%m.%Y')


    def __str__(self):
        if(self.value):
            return self.value.strftime('%d.%m.%Y')
        else:
            return ''


    def __iter__(self):
        """Iterate over attributes"""
        yield self.value
        

class Record:
    """ element of record for address book """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None


    def add_phone(self, phone:str) -> None:
        """ add phone to list """
        try:
            self.phones.append(Phone(phone))
        except ValueError:
            print('Phone validation failed, the phone must have 10 digits and consist only of numbers')
            sys.exit(0)


    def edit_phone(self, old, new):
        """ edit phone into phones list """
        # check if exists
        obj = self.find_phone(old)
        if obj:
            # remove old phone
            self.remove_phone(obj)
            # add new phone
            self.add_phone(new)


    def remove_phone(self, phone):
        """ remove phone from phones list """ 
        self.phones.remove(phone)


    def find_phone(self, phone):
        """ find phone into list """            
        for item in self.phones:
            if phone == item.value:
                return item
        # if nothing is found
        return False


    def add_birthday(self, birthday) -> None:
        """ add birthday """
        try:
            # insert date of birth
            if self.birthday is None:
                self.birthday = Birthday(birthday)
                return 'Birthday added'
            # update date of birth
            elif self.birthday:
                self.birthday = Birthday(birthday)
                return 'Birthday was updated'
            else:
                return False
        except ValueError:
            print('Birthday validation failed, the birthday should have next format DD.MM.YYYY')
            sys.exit(0)


    def __str__(self):
        """ string representation """
        return f"Contact name: {self.name}, Contact phones: {'; '.join(str(p) for p in self.phones)}, Contact birthday: {self.birthday}"


    def __iter__(self):
        """Iterate over attributes"""
        yield self.name
        yield from self.phones
        yield from self.birthday


class AddressBook(UserDict):
    """ adress book class """

    def add_record(self, record):
        """ add record into dict, record has name and phones """
        self.data[record.name] = record


    def find(self, fname):
        """ find name """
        for name in self.data:
            if name.value == fname:
                return self.data[name]
        return None


    def delete(self, key):
        """ delete somenthing from user dictionary """
        remove = None
        for item in self.data:
            if key == item.value:
                remove = item
                break
        # remove element from dictionary
        self.data.pop(remove)


    def get_upcoming_birthdays(self) -> dict:
        """ get birthdays list """
        result = []
        today = datetime.today().date()
        for item in self.data.items():
            # item -> name, record
            name, record = item
            # record -> name, phone, birthday(2000-05-25 00:00:00)
            contact_name, contact_phones, contact_birthday = record
            # get datatime object from str
            b_obj = contact_birthday.date() # 2000-05-25
            # get day of year (birthday) - 122
            day_of_year = b_obj.timetuple().tm_yday
            # get day of year (today) - 119
            day_of_year_current = today.timetuple().tm_yday
            # its one week
            one_week = day_of_year_current+7
            # get date witch
            if day_of_year >= day_of_year_current and one_week >= day_of_year:
                modified_birthday = b_obj.replace(year = today.year)
                # check if weekend
                if modified_birthday.weekday() == 5 or modified_birthday.weekday() == 6:
                    # modified to next monday
                    delta = (6 - modified_birthday.weekday()+1) % 6
                    modified_birthday = modified_birthday + timedelta(days=delta)
                result.append(record)

        return result   