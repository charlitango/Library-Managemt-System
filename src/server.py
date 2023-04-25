import json
import socket
import logging
import time
import custom_code
import common
import custom_exceptions
from registration_form import RegistrationForm
from Models.user import User
"""
set logging level to DEBUG
server_logs.log : Store logs in this file
filemode=w : override file logs each time
"""
logging.basicConfig(filename='logs/server_logs.log', filemode='w',
                    level=logging.DEBUG)

# create logging object
logger = logging.getLogger()

""" 
create socket object for client
AF_INET : IPv4
SOCK_STREAM : TCP
"""

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info("server socket created")
except socket.error as err:
    logger.error(f"error in socket creation: {err}")

# bind socket over localhost
host = 8084
try:
    server_socket.bind(('127.0.0.1', host))
    logger.info(f"server bind to host: {host}")
except socket.error as err:
    logger.error(f"Could not bind to host {host} : {err}")

# put socket in listening mode
server_socket.listen(5)
logger.info("server listening")

# initialize connection with client
client_object, address = server_socket.accept()
logger.info(f"Got connection from {address}")
client_object.send("welcome to Library Management System !!!!".encode())


while True:
    login_flag = False

    if not login_flag:
        menu = RegistrationForm.display_operations()
        common.encode_data(client_object, menu)
        choice = common.decode_data(client_object)

        if choice == '1':
            common.encode_data(client_object, "Enter username")
            username = common.decode_data(client_object)
            common.encode_data(client_object, "Enter password")
            password = common.decode_data(client_object)
            form = RegistrationForm(username, password)
            try:
                user_object = form.sign_in()
                if user_object:
                    login_flag = True
                    # common.encode_data(client_object, user_object)
                    # menu = RegistrationForm.display_operations(user_object.role)
                    # time.sleep(1)
                    # common.encode_data(client_object, str(menu))
                    # # send status code at last
                    # time.sleep(1)
                    # common.encode_data(client_object, custom_code.codes[0])

                    menu = RegistrationForm.display_operations(user_object.role)
                    user_object_as_dict = vars(user_object)
                    user_object_dump = json.dumps(user_object_as_dict)
                    common.encode_data(client_object, user_object_dump)
                    time.sleep(1)
                    common.encode_data(client_object, str(menu))
                    # send status code at last
                    time.sleep(1)
                    common.encode_data(client_object, custom_code.codes[0])
                else:
                    raise custom_exceptions.InvalidCredentialsError(custom_code.codes[3])
            except custom_exceptions.InvalidCredentialsError as invalid:
                common.encode_data(client_object, str(invalid.args[0]))
            except:
                # internal server error
                common.encode_data(client_object, str(custom_code.codes[4]))

        if choice == '2':
            common.encode_data(client_object, "Enter username")
            username = common.decode_data(client_object)
            common.encode_data(client_object, "Enter password")
            password = common.decode_data(client_object)
            common.encode_data(client_object, "Enter Email")
            email = common.decode_data(client_object)
            form = RegistrationForm(username, password, email)
            try:
                code = form.sign_up()
                if code == custom_code.codes[1]:
                    common.encode_data(client_object, str(custom_code.codes[1]))
                if code == custom_code.codes[2]:
                    raise custom_exceptions.UserExistsError(custom_code.codes[2])
            except custom_exceptions.UserExistsError as user_err:
                common.encode_data(client_object, str(user_err.args[0]))
            except:
                # internal server error
                common.encode_data(client_object, str(custom_code.codes[4]))
            else:
                login_flag = False

    if login_flag:
        recv_object = common.decode_data(client_object)
        recv_object_json = json.loads(recv_object)
        if recv_object:
            common.encode_data(client_object, "Enter choice")
            choice = common.decode_data(client_object)

            if choice == 3:
                user_object = None
                login_flag = False

            if choice == '4':
                pass