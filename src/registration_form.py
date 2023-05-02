import custom_code
from Models.user import User


class RegistrationForm:

    def __init__(self, *args):
        if len(args) == 2:
            self.username = args[0]
            self.password = args[1]
        if len(args) == 3:
            self.username = args[0]
            self.password = args[1]
            self.email = args[2]

    @staticmethod
    def display_operations(role=None):
        if role == "student":
            return {
                '3': 'logout',
                '4': 'Display available books',
                '5': 'Order book',
                '6': 'Donate book',
                '7': 'Return book'
            }
        if role == "admin":
            return {
                '3': 'logout',
                '4': 'Display available books',
                '5': 'Order book',
                '6': 'Donate book',
                '7': 'Return book',
                '8': 'Book/s Issued',
                '9': 'check penalty'
            }
        if role is None:
            return {
                '1': 'Sign In',
                '2': 'Sign Up',
            }

    def sign_in(self):
        usr = User(self.username, self.password)
        data = usr._User__get_user_attributes()
        usr_status = usr._User__validate_credentials(self.username, self.password, data)
        return usr_status

    def sign_up(self):
        usr = User(self.username, self.password, self.email)
        data = usr._User__get_user_attributes()
        usr_status = usr._User__validate_credentials(self.username, self.password, data)
        if usr_status:
            return custom_code.codes[2]
        else:
            usr._User__add_user_in_file()
            return custom_code.codes[1]
