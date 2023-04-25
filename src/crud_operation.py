"""" add admin details"""

import uuid

role = "admin"

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

sample_data = [
]

""" add book details """




