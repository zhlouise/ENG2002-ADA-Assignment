#Creating class for user login application
class login:
    def __init__(self, username = '', password= ''):
        self.username = username
        self.password = password

    def check_username(self):
        #assigning i = 5 for 5 attempts for the password
        i = 5
        self.username = input("Enter your username: ") 
        found = False
        with open('login_info.txt', 'r') as f:             #opening/creating a txt file for storing username and password data
            lines = [line.strip().split(',') for line in f] #splitting every line in two elements of a list. [0] for username [1] for password.
        for line in lines:
            if line[0] == self.username:    #if username exists, checking whether the password from the user matches the record 
                found = True
                while i > 0:
                    self.password = input("Enter your password: ")
                    if line[1] == self.password:
                        print("Login Successful!")
                        return 1
                    else:
                        if i > 1:
                            i -= 1
                            print(f'Invalid Username/Password! Try again. {i} attempts left.') #This portion will run untill i becomes 0. 5 total attempts for the user.
                        else:
                            print("Failed to enter the correct password! Application quit.")
                            return 2
        if not found:
            self.password = input("Create a password: ") #if username is new, appending new username + password in the txt file
            with open('login_info.txt', 'a') as f:
                f.write(f"{self.username},{self.password}\n")
            print("Account Created!")
            return 1
        

