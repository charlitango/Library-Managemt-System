import csv
import uuid


file = 'C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\user_data.csv'


class User:

    def __init__(self, *args):
        if len(args) == 2:
            self._user_id = None
            self._username = args[0]
            self._password = args[1]
            self._role = None
            self._email = None
        if len(args) == 3:
            self._user_id = None
            self._username = args[0]
            self._password = args[1]
            self._role = None
            self._email = args[2]
        if len(args) == 5:
            self._user_id = args[0]
            self._username = args[1]
            self._password = args[2]
            self._role = args[3]
            self._email = args[4]

    def __get_user_attributes(self):
        users = []
        with open(file, 'r') as f:
            next(f)
            csv_reader = csv.reader(f)
            for record in csv_reader:
                if record:
                    users.append(User(record[0], record[1], record[2],
                                      record[3], record[4]))
        return users

    def __add_user_in_file(self):
        role = "student"
        uid = uuid.uuid1()
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([uid, self._username, self._password, role,
                            self._email])

    def __validate_credentials(self, username, password, data):
        for record in data:
            if username == record.user_name and password == record.password:
                return record
        else:
            return None

    def __validate_client_object(self, client):
        all_users = self.__get_user_attributes()
        for user in all_users:
            if user is client:
                return True
        return False


    @property
    def user_id(self):
        return self._user_id

    @property
    def user_name(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role

    @property
    def email(self):
        return self._email
