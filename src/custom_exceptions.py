class InvalidCredentialsError(Exception):

    def __int__(self, val):
        self.err_code = val

    def __str__(self):
        return repr(self.err_code)


class UserExistsError(Exception):

    def __int__(self, val):
        self.err_code = val

    def __str__(self):
        return repr(self.err_code)