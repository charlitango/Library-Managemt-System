import csv

book_file = 'C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src\\csvfiles\\book.csv'


class Book:

    def __init__(self, *args):
        if len(args) == 4:
            self._book_id = args[0]
            self._book_name = args[1]
            self._author = args[2]
            self._count = args[3]

        if len(args) == 3:
            self._book_name = args[0]
            self._author = args[1]
            self._count = args[2]

    def __get_book_details(self):
        books = []
        with open(book_file, 'r') as f:
            reader = csv.reader(f)
            for record in reader:
                if record:
                    books.append(
                        Book(record[0], record[1], record[2], record[3]))
        return books

    def __display_books(self):
        books = self.__get_book_details()
        book_details_display = []
        for record in books:
            if record:
                book_details_display.append(
                    Book(record._book_name, record._author, record._count)
                )
        return book_details_display

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