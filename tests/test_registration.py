import sys
import os

path = os.path.abspath("C:\\Users\\141573\\PycharmProjects\\LibraryManagementSystem\\src")
sys.path.append(path)

import registration_form


class TestSignIn:

    def test_valid_credentials(self):
        registration = registration_form.RegistrationForm('abc', 'abc@123')
        data = registration.sign_in()
        msg = data[0]
        assert msg == "login successful"

    def test_invalid_credentials(self):
        registration = registration_form.RegistrationForm('Tango', 'Charli')
        data = registration.sign_in()
        msg = data[0]
        assert msg == "Invalid credentials"

    def test_sign_up(self):
        pass

    def test_sign_up_exising_user(self):
        pass

    def test_logout(self):
        pass






