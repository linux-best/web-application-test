import pytest
from tests import *

def test_login():
    assert login_test_section(login_user="admin",login_passwd="123") == "login passed !"

def test_CSRF():
    assert CSRF_Test_section(new_paassword="password") == "Password Changed !"

def test_Brute_Force():
    assert Brute_Force_Test_section(username="admin",password="123") == "Welcome to the password protected area admin !"

def test_Driver_quit():
    assert driver_quit() == "Done !"


#def test_Brute_Force():
#    assert Brute_Force_Test(username_file="username.txt",password_file="password.txt") ==  "login passed !"