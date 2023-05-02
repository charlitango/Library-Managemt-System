import json
import socket
import logging
import uuid

import common
import custom_code
"""
set logging level to DEBUG
server_logs.log : Store logs in this file
filemode=w : override file logs each time
"""
logging.basicConfig(filename='logs/client_logs.log', filemode='w',
                    level=logging.DEBUG)

# create logger object
logger = logging.getLogger()

""" 
create socket object for client
AF_INET : IPv4
SOCK_STREAM : TCP
"""
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("server socket created")
except socket.error as err:
    logger.error(f"error in socket creation: {err}")

host = 8084

# connect to the server on localhost
client_socket.connect(('127.0.0.1', host))

# accept welcome message
recv_data = client_socket.recv(1024).decode()
logger.info(recv_data)
print(recv_data)

registration_choice = ['1', '2']
student_choice = ['3', '4', '5', '6', '7']
admin_choice = student_choice + ['8', '9', '10']


while True:
    login_flag = False

    if not login_flag:
        print(common.decode_data(client_socket))
        choice = input("Enter choice: ")
        while choice not in registration_choice:
            choice = input("Enter valid choice: ")
        common.encode_data(client_socket, choice)

        if choice == '1':
            print(common.decode_data(client_socket))
            username = input()
            common.encode_data(client_socket, username)
            print(common.decode_data(client_socket))
            password = input()
            common.encode_data(client_socket, password)
            user_object = common.decode_data(client_socket)
            user_object_dict = json.loads(user_object)
            if user_object and not user_object.isnumeric():
                login_flag = True
                menu = common.decode_data(client_socket)
                print(menu)
                status_code = common.decode_data(client_socket)
                print(custom_code.eval_status_codes[status_code])
            if user_object and user_object.isnumeric():
                print(custom_code.eval_status_codes[user_object])

        elif choice == '2':
            print(common.decode_data(client_socket))
            username = input()
            common.encode_data(client_socket, username)
            print(common.decode_data(client_socket))
            password = input()
            common.encode_data(client_socket, password)
            print(common.decode_data(client_socket))
            email = input()
            common.encode_data(client_socket, email)
            status_code = common.decode_data(client_socket)
            print(custom_code.eval_status_codes[status_code])

    while login_flag:
        user_object_json = json.dumps(user_object_dict)
        common.encode_data(client_socket, user_object_json)
        print(common.decode_data(client_socket))
        choice = input()

        if user_object_dict['_role'] == "student":
            while choice not in student_choice:
                choice = input("Enter valid choice: ")
        if user_object_dict['_role'] == "admin":
            while choice not in admin_choice:
                choice = input("Enter valid choice: ")

        common.encode_data(client_socket, choice)

        if choice == '3':
            user_object_loaded = None
            login_flag = False

        if choice == '4':
            data = common.decode_data(client_socket)
            if data.isnumeric():
                print(custom_code.eval_status_codes[data])
            else:
                json_data = json.loads(data)
                print("*****************************************************************")
                for record in json_data:
                    print(
                        f"book id: {record['_book_id']} ==>  book:{record['_book_name']} ==> author:{record['_author']}  ==> available copies:{record['_count']}"
                    )
                print("******************************************************************")

        if choice == '5':
            data = common.decode_data(client_socket)
            if data.isnumeric():
                print(custom_code.eval_status_codes[data])
            else:
                json_data = json.loads(data)
                for record in json_data:
                    print(
                        f"book id: {record['_book_id']} ==>  book:{record['_book_name']} ==> author:{record['_author']}  ==> available copies:{record['_count']}"
                    )
                print(common.decode_data(client_socket))
                book_id = input("")
                common.encode_data(client_socket, book_id)
                print(common.decode_data(client_socket))
                count = input("")
                common.encode_data(client_socket, count)
                status_code = common.decode_data(client_socket)
                if status_code.isnumeric():
                    print(custom_code.eval_status_codes[status_code])
                else:
                    print(status_code)

        if choice == '6':
            print(common.decode_data(client_socket))
            book_name = input("Enter book name: ")
            author = input("Enter Author name: ")
            count = input("Enter number of copies: ")
            book_details = {
                'data': [book_name, author, count]
            }
            book_details_json = json.dumps(book_details)
            common.encode_data(client_socket, book_details_json)
            status_code = common.decode_data(client_socket)
            print(custom_code.eval_status_codes[status_code])

        if choice == '7':
            print("Details of book issued to you in format: {book id: number of copies}")
            print(common.decode_data(client_socket))
            print("Enter book details to return: ")
            book_id = input("Enter book id: ")
            no_of_copies = input("Enter number of copies: ")
            book_details = {
                'data': [book_id, no_of_copies]
            }
            json_data = json.dumps(book_details)
            common.encode_data(client_socket, json_data)
            status_code = common.decode_data(client_socket)
            print(custom_code.eval_status_codes[status_code])
