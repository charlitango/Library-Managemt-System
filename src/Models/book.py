import csv
import os
import sys
import uuid

import pandas as pd

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from custom_code import codes

book_file = 'C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\book.csv'


class Book:

    def __init__(self, *args):
        if len(args) == 4:
            self._book_id = args[0]
            self._book_name = args[1]
            self._author = args[2]
            self._count = args[3]

    def __get_book_details(self):
        books = []
        with open(book_file, 'r') as f:
            next(f)
            reader = csv.reader(f)
            for record in reader:
                if record:
                    books.append(
                        Book(record[0], record[1], record[2], record[3]))
        return books

    def __write_book_details(self, book_data, is_donate=False, is_return=False, is_issue=False):
        books = self.__get_book_details()
        loop_counter = 0
        for record in books:
            if is_donate:
                if record.book_name == book_data[0] and record.author == book_data[1]:
                    book_id = record.book_id
                    df_book_csv = pd.read_csv(book_file)
                    df_book_csv['count'][loop_counter] = df_book_csv['count'][loop_counter] + int(book_data[2])
                    df_book_csv.to_csv(book_file, index=False)
                    return book_id
                loop_counter = loop_counter + 1
            elif is_return:
                if record.book_id == book_data[0]:
                    df_book_csv = pd.read_csv(book_file)
                    df_book_csv['count'][loop_counter] = df_book_csv['count'][loop_counter] + int(book_data[1])
                    df_book_csv.to_csv(book_file, index=False)
                    return book_data[0]
                loop_counter = loop_counter + 1
            elif is_issue:
                if record.book_id == book_data[0]:
                    df_book_csv = pd.read_csv(book_file)
                    df_book_csv['count'][loop_counter] = df_book_csv['count'][loop_counter] - int(book_data[1])
                    df_book_csv.to_csv(book_file, index=False)
                    return book_data[0]
                loop_counter = loop_counter + 1
        else:
            if is_donate:
                book_id = uuid.uuid1()
                with open(book_file, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        book_id, book_data[0], book_data[1], book_data[2]
                    ])
                return book_id
            if is_return:
                return codes[11]

    def __validate_book_order(self, book_id, count):
        books = self.__get_book_details()
        is_book_details_valid = False
        for record in books:
            if record.book_id == book_id:
                if int(record.count) == 0:
                    return codes[7], is_book_details_valid
                if int(record.count) < int(count):
                    return codes[6], is_book_details_valid
                if int(record.count) > int(count):
                    is_book_details_valid = True
                    return None, is_book_details_valid
        else:
            return codes[5], is_book_details_valid

    @property
    def book_id(self):
        return self._book_id

    @property
    def book_name(self):
        return self._book_name

    @property
    def author(self):
        return self._author

    @property
    def count(self):
        return self._count

if __name__ == '__main__':
    b = Book()
    b._Book__display_books()