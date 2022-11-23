#CYB135 Week 1 Lab 1.12
'''
1.12 Lab: Check Login Credentials (classes)
Complete the Login class implementation. For the class method check_credentials(), you will need to
accept two arguments - login and passwd. Do not forget about the self argument.

This class method will set two local variables simlogin = "Test" and simpass = "test1234".
These variables will simulate the correct login and password for the credential check process.

The method will receive the login and password from the user and check it with Test and test1234.
If the user sent the correct credentials output:

Successful login!

If the user sent the correct login name but the wrong password output:

Login name is correct, incorrect password!

If the user sent an incorrect login name but the correct password output:

Login name is incorrect, password accepted!

If the user sent both incorrect login name and password output:

Unsuccessful login attempt!

The class method will return a boolean success variable as True if the login was successful.

Using if __name__ == "__main__" to control the flow of your code, add a loop that will stop the process if the
user attempts more than 5 login attempts.

Ex: If the input is:

Testit
test
And this is their first incorrect attempt. The output is:

Unsuccessful login attempt!
Try again - you have 4 attempts left!

If the input is:

Test
test1234
The output is:

Successful login!
'''

class Login:
        def __init__(self):
                self.login_name = 'none'
                self.login_password = 'none'
        def check_credentials(self, user_login, user_passwd):
                simlogin = 'Test'
                simpass = 'test1234'

                if user_login == simlogin and user_passwd == simpass:
                        print("Successful login!")
                        return True
                elif user_login == simlogin and user_passwd != simpass:
                        print("Login name is correct, incorrect password!")
                        return False
                elif user_login != simlogin and user_passwd == simpass:
                        print("Login name incorrect, password accepted!")
                        return False
                elif user_login != simlogin and user_passwd != simpass:
                        print(user_login,user_passwd)
                        #print("Unsuccessful login attempt!")
                        return False
if __name__ == "__main__":
    login_obj = Login()
    timeout = 5

    for i in range(1,timeout+1):
        login = input()
        password = input()
        check_login = login_obj.check_credentials(login, password)

        if check_login == True:
            print("Successful login!")
            break
        elif check_login == False:
            print("Unsuccessful login attempt!")
            if i !=timeout:
                print(f"Try again - you have  {timeout-i} attempts left!")
