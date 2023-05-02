def encode_data(obj, data):
    obj.send(str(data).encode())


def decode_data(obj):
    return obj.recv(2048).decode()

