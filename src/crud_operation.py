import csv
import uuid

user_file = 'C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\demo.csv'
book_file = 'C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\book.csv'
role = "admin"


class CRUDOperations:

    def __int__(self):
        pass

    @staticmethod
    def __add_admin_details():
        unique_id = []
        uname = []
        passwd = []
        emails = []

        for i in range(5):
            idd = uuid.uuid1()
            username = f"admin{idd}"
            password = f"admin{idd}@123"
            email = f"{username}@gmail.com"
            unique_id.append(idd)
            uname.append(username)
            passwd.append(password)
            emails.append(email)

        with open(user_file, 'w') as f:
            writer = csv.writer(f)
            for i in range(5):
                writer.writerow([unique_id[i], uname[i], passwd[i],
                                 "admin", emails[i]])

    def __add_book_details(self):
        book_id = []
        book_name = ["Advanced Python", "Django", "AWS", "C++", "Java Script"]
        author = ["John", "Bob", "Stephane", "Alis", "Paul"]
        book_count = [5, 7, 10, 5, 5]

        for i in range(5):
            book_uid = uuid.uuid1()
            book_id.append(book_uid)

        with open(book_file, 'a+') as f:
            writer = csv.writer(f)
            for i in range(len(book_id)):
                writer.writerow([book_id[i], book_name[i], author[i],
                                 book_count[i]])

obj = CRUDOperations()
obj._CRUDOperations__add_book_details()