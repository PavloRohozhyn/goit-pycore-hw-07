""" validation module """
import re
from errors import error_name_validation, error_phone_validation, \
    error_name_doesnt_exists, error_name_exists

from classes import Name


def input_error(func):
    """ decorator - validation arguments structure """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return ["Give me name and phone please."]
        except IndexError:
            return ["Index error"]
        except KeyError:
            return ["Key Error"]

    return inner


def validation_for_add_function(func):
    """ 
    decorator - validation params for "ADD" function
     - contact_name
     - phone_number
     - contact_name exists
     - phone_number exists 
    """

    def wrapper(*args, **kwargs):
        """ handle params """
        try:
            # ([name, phone], {contact book})
            data, *_ = args
            name, phone = data
            # check first value - name
            if not check_contact_name(name):
                raise ValueError(error_name_validation())
            # check second value - phone
            elif not check_phone_number(phone):
                raise ValueError(error_phone_validation())
            else:
                pass
            return func(*args, **kwargs)
        except ValueError as e:
            return f'{e}'
        except TypeError:
            return 'Please enter "contact_name" and "phone_number"'

    return wrapper


def validation_for_change_function(func):
    """ 
    decorator - validation params for "CHANGE" function
     - contact_name
     - old phone_number
     - new phone_number
     - contact_name exists
     - phone_number exists 
    """
    def wrapper(*args, **kwargs):
        """ handle params """
        try:
            # (['foo', '1111111111', '2222222222'], {<classes.Name object at 0x7d2b84f935b0>: <classes.Record object at 0x7d2b84f93460>})
            data, contacts = args
            name, old, new  = data
            # check first value - name
            if not check_contact_name(name):
                raise ValueError(error_name_validation())
            # check second value - old phone
            elif not check_phone_number(old):
                raise ValueError(error_phone_validation())
            # check third value - new phone
            elif not check_phone_number(new):
                raise ValueError(error_phone_validation())
            # check if contact_name doesnt exists
            elif not check_contact_name_exists(name, contacts):
                raise ValueError(error_name_doesnt_exists(name))
            else:
                pass
            return func(*args, **kwargs)
        except ValueError as e:
            return f'v {e}'
        except TypeError as e:
            return f'Please enter "contact_name" and "phone_number {e}"'
    return wrapper


def validation_for_show_function(func):
    """ 
    decorator - validation params for "show" function 
     - phone_number
     - contact_name doesnt exists
    """
    def wrapper(*args, **kwargs):
        """ handle params """
        try:
            # ([name], {contact book})
            data, contacts = args
            name, = data
            # check contact name
            if not check_contact_name(name):
                raise ValueError(
                    error_name_validation())
            # check if contact name doesnt exists
            elif not check_contact_name_exists(name, contacts):
                raise ValueError(
                    error_name_doesnt_exists(name))
            else:
                pass
            return func(*args, **kwargs)
        except ValueError as e:
            return f'{e}'
        except TypeError:
            return 'Please enter "contact_name"'

    return wrapper


def check_contact_name(name: str) -> bool:
    """ validation contact_name """
    if re.match(r'^[a-zA-Z]+$', name):
        return True
    else:
        return False


def check_phone_number(phone: str) -> bool:
    """ validation phone_number """
    if re.match(r'^[0-9]+$', phone):
        return True
    else:
        return False


def check_contact_name_exists(name: str, contacts) -> bool:
    """ check if contact_name exists into contact book """
    for item in contacts:
        if isinstance(item, Name) and item.value == name:
            return True
        else:
            return False
    return False


def check_phone_number_exists(phone: str, contacts) -> bool:
    """ check if phone_number exists into contact book """
    if phone in contacts.values():
        return True
    else:
        return False
