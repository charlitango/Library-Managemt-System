import uuid
from Models.book import Book
from Models.transaction import Transaction, RecordTransactionArgs
from custom_code import  codes


class Library:

    def __init__(self):
        pass

    def display_books(self):
        book_object = Book()

        return book_object._Book__get_book_details()

    def order_book(self, book_id, count, user_object):
        book_object = Book()
        status_code, is_book_details_valid = book_object._Book__validate_book_order(book_id, count)
        if is_book_details_valid:
            book_object = Book()
            book_id = book_object._Book__write_book_details([book_id, count], is_issue=True)
            trans = Transaction()
            transaction_details = trans._Transaction__get_transaction_details()
            trans_args = RecordTransactionArgs()
            trans_args.set_user_object(user_object)
            trans_args.set_book_id(book_id)
            trans_args.set_book_count(count)
            trans_args.set_transaction_details(transaction_details)
            trans_args.set_is_issued(True)

            return trans._Transaction__record_transaction(trans_args, issue_book=True)

        if status_code:
            return status_code

    def return_book(self, book_details_json, user_object):
        book_data = book_details_json['data']
        book_object = Book()
        book_id = book_object._Book__write_book_details(book_data, is_return=True)
        if book_id == codes[11]:
            return book_id
        trans = Transaction()
        transaction_details = trans._Transaction__get_transaction_details()
        trans_args = RecordTransactionArgs()
        trans_args.set_user_object(user_object)
        trans_args.set_book_id(book_id)
        trans_args.set_book_count(book_data[1])
        trans_args.set_transaction_details(transaction_details)
        return trans._Transaction__record_transaction(trans_args, lets_return=True)

    def donate_book(self, book_details_json, user_object):
        book_data = book_details_json['data']
        book_object = Book()
        book_id = book_object._Book__write_book_details(book_data, is_donate=True)
        trans = Transaction()
        transaction_details = trans._Transaction__get_transaction_details()
        trans_args = RecordTransactionArgs()
        trans_args.set_user_object(user_object)
        trans_args.set_book_id(book_id)
        trans_args.set_book_count(book_data[2])
        trans_args.set_transaction_details(transaction_details)

        return trans._Transaction__record_transaction(trans_args, lets_donate=True)

    def show_issued_books(self, user_object=None, many=False):
        trans = Transaction()
        transaction_details = trans._Transaction__get_transaction_details()
        if user_object:
            for record in transaction_details:
                if record.user_id == user_object['_user_id']:
                    return record.book_name, record.no_of_copies_issued
        if many:
            issued_book_details = []
            for record in transaction_details:
                each_record = [record.user_id, record.book_name, record.no_of_copies_issued]
                issued_book_details.append(each_record)
            return issued_book_details

    def check_student_penalty(self):
        trans = Transaction()
        transaction_details = trans._Transaction__get_transaction_details()
        return trans._Transaction__check_penalty(transaction_details)


