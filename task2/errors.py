"""
module errors
"""

# def error_args(e):
#     """ when command doesn't have enough arguments """

#     return f"Error: maybe, you forgot to pass arguments into command ({e})"


# def error_item_exist(name):
#     """ when item exists into contact list """

#     return f"Name ({name}) already exists, use (change) command to edit data"


# def error_item_doesnt_exist(name):
#     """ when item doesnt exists into contact list """

#     return f'Name {name} doesnt exists in contact list, use (add) command to add contact into contact list'


# def error_validation_name(name):
#     """ validation contact name """

#     return f'Invalid contact name ({name}) was passed'



def error_name_validation():
    """ regex name validation """
    return 'Invalid contact_name was passed'


def error_phone_validation():
    """ regex phone validation """
    return 'Invalid phone_number was passed'


def error_name_doesnt_exists(name):
    """ contact_name doesnt exists """
    return f'The ({name}) doesnt exists, use command - "add" for changing contact data'


def error_name_exists(name):
    """ contact_name already exists """
    return f'The ({name}) already exists, use command - "change" for changing contact data'