import json
import socket
import logging
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

    if login_flag:
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
            pass









