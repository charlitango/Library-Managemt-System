import csv
import os
import sys
import pandas as pd
from datetime import datetime, timedelta
file = "C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\transaction.csv"
book_csv = "C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\book.csv"


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from custom_code import codes


class RecordTransactionArgs:

    def __init__(self, user_object='NA', book_id='NA', count='NA', transaction_details='NA',
                 is_issued=False, is_returned=False, is_donated=False, issue_date='NA', return_date='NA',
                 donate_date='NA'):
        self._user_object = user_object
        self._book_id = book_id
        self._count = count
        self._transaction_details = transaction_details
        self._is_issued = is_issued
        self._is_returned = is_returned
        self._is_donated = is_donated
        self._issue_date = issue_date
        self._return_date = return_date
        self._donate_date = donate_date

    @property
    def user_object(self):
        return self._user_object

    @property
    def book_id(self):
        return self._book_id

    @property
    def count(self):
        return self._count

    @property
    def transaction_details(self):
        return self._transaction_details

    @property
    def is_issued(self):
        return self._is_issued

    @property
    def is_returned(self):
        return self._is_returned

    @property
    def is_donated(self):
        return self._is_donated

    @property
    def issue_date(self):
        return self._issue_date

    @property
    def return_date(self):
        return self._return_date

    @property
    def donate_date(self):
        return self._donate_date

    def set_user_object(self, user_object):
        self._user_object = user_object

    def set_book_id(self, book_id):
        self._book_id = book_id

    def set_book_count(self, book_count):
        self._count = book_count

    def set_transaction_details(self, transaction_details):
        self._transaction_details = transaction_details

    def set_is_issued(self, flag):
        self._is_issued = flag

    def set_is_returned(self, flag):
        self._is_returned = flag

    def set_is_donated(self, flag):
        self._is_donated = flag


class Transaction:

    def __init__(self, *args):
        if len(args) == 10:
            self._user_id = args[0]
            self._role = args[1]
            self._book_name = args[2]
            self._no_of_copies_issued = args[3]
            self._is_issued = args[4]
            self._is_returned = args[5]
            self._is_donated = args[6]
            self._issue_date = args[7]
            self._return_date = args[8]
            self._donate_date = args[9]
        if len(args) == 0:
            self._user_id = None
            self._role = None
            self._book_name = None
            self._no_of_copies_issued = None
            self._is_issued = None
            self._is_returned = None
            self._is_donated = None
            self._issue_date = None
            self._return_date = None
            self._donate_date = None

    @property
    def user_id(self):
        return self._user_id

    @property
    def role(self):
        return self._role

    @property
    def book_name(self):
        return self._book_name

    @property
    def no_of_copies_issued(self):
        return self._no_of_copies_issued

    @property
    def is_issued(self):
        return self._is_issued

    @property
    def is_returned(self):
        return self._is_returned

    @property
    def is_donated(self):
        return self._is_donated

    @property
    def return_date(self):
        return self._return_date

    @property
    def issue_date(self):
        return self._issue_date

    @property
    def donate_date(self):
        return self._donate_date

    def __get_transaction_details(self):
        transaction_details = []
        with open(file, 'r') as f:
            next(f)
            reader = csv.reader(f)
            for record in reader:
                if record:
                    transaction_details.append(
                        Transaction(record[0], record[1], record[2], record[3],
                                    record[4], record[5], record[6], record[7],
                                    record[8], record[9])
                    )
        return transaction_details

    def __write_transaction_details(self, filename, mode, trans_object, issue_book,
                                    lets_return, lets_donate):
        if mode == 'a':
            trans_object._issue_date = datetime.now()
            with open(filename, mode) as f:
                writer = csv.writer(f)
                writer.writerow(
                    [trans_object.user_object['_user_id'], trans_object.user_object['_role'],
                     trans_object._book_id, trans_object._count, trans_object._is_issued,
                     trans_object._is_returned, trans_object._is_donated, trans_object._issue_date,
                     trans_object._return_date, trans_object._donate_date ])

            return codes[8]

        if mode == 'w+':
            df = pd.read_csv(filename)

            if issue_book:
                loop_counter = 0
                for record in trans_object.transaction_details:
                    if record.user_id == trans_object.user_object['_user_id']:
                        df['is_issued'][loop_counter] = True
                        df['no_of_copies_issued'][loop_counter] = trans_object._count
                        df['issue_date'][loop_counter] = datetime.now()
                        df['return_date'][loop_counter] = 'NA'
                    loop_counter = loop_counter + 1
                df.to_csv(book_csv, index=False)
                return codes[8]

            if lets_return:
                loop_counter = 0
                for record in trans_object.transaction_details:
                    if record.user_id == trans_object.user_object['_user_id']:
                        difference = int(record.no_of_copies_issued) - int(trans_object.count)
                        if difference < 0 or int(record.no_of_copies_issued) == 0:
                            return codes[12]
                        if difference == 0:
                            df['is_issued'][loop_counter] = False
                            df['issue_date'][loop_counter] = 'NA'
                        df['no_of_copies_issued'][loop_counter] = difference
                        df['is_returned'][loop_counter] = True
                        df['return_date'][loop_counter] = datetime.now()
                    loop_counter = loop_counter + 1
                df.to_csv(filename, index=False)
                return codes[9]

            if lets_donate:
                loop_counter = 0
                for record in trans_object.transaction_details:
                    if record.user_id == trans_object.user_object['_user_id']:
                        df['is_donated'][loop_counter] = True
                        df['donate_date'][loop_counter] = datetime.now()
                    loop_counter = loop_counter + 1
                df.to_csv(filename, index=False)
                return codes[10]

    def __check_user_record(self, trans_object):
        for record in trans_object.transaction_details:
            if record.user_id == trans_object.user_object['_user_id']:
                if record.is_issued:
                    start = datetime.strptime(record.issue_date, "%Y-%m-%d %H:%M:%S.%f")
                    expiry = start + timedelta(days=7)
                    today = datetime.now()
                    if expiry > today:
                        expiry_date = expiry - today
                        return f"Please return issued book within {expiry_date.days} days to order next book"
                    if expiry < today:
                        due_date = today - expiry
                        due_days = due_date.days
                        return f"Please return issued and pay penalty RS.{due_days * 20} to order next book"

    def __record_transaction(self, trans_object, issue_book=False,
                             lets_return=False, lets_donate=False):
        for record in trans_object.transaction_details:
            if record.user_id == trans_object.user_object['_user_id']:
                if issue_book:
                    due_record = self.__check_user_record(trans_object)
                    if not due_record:
                        return self.__write_transaction_details(file, 'w+', trans_object, issue_book,
                                                                lets_return, lets_donate)
                    else:
                        return due_record

                if lets_donate:
                    return self.__write_transaction_details(file, 'w+', trans_object, issue_book,
                                                            lets_return, lets_donate)

                if lets_return:
                    return self.__write_transaction_details(file, 'w+', trans_object, issue_book,
                                                            lets_return, lets_donate)

        else:
            return self.__write_transaction_details(file, 'a', trans_object, issue_book,
                                                    lets_return, lets_donate)


    def __check_penalty(self, transaction_details):
        res = []
        for record in transaction_details:
            if record:
                if record.is_issued == 'True':
                    start = datetime.strptime(record.issue_date, "%Y-%m-%d %H:%M:%S.%f")
                    expiry = start + timedelta(days=7)
                    today = datetime.now()
                    if expiry > today:
                        res.append([record.user_id, 'NA'])
                    if expiry < today:
                        due_date = today - expiry
                        due_days = due_date.days
                        res.append([record.user_id, f"{due_days * 20}"])
        return res