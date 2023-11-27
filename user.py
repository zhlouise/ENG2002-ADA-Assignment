# Create a class representing a user of the application
class user:
  # Initialize a user object with a username
  def __init__(self, username, password): 
    self.username = username
    self.password = password
    # Create and append a storage file for storing all the username and password pairs
    storage_file = open("username_password.txt", "w")
    # Write the username & password pair into the storage file
    storage_file.write("{},{}/n".format(username, password))
    storage_file.close() # Close the storage file

  # Method to check whether a user already exists or not
  def check_username(username, storage_file):
    storage_file = open("username_password.txt", "r")
    for user in users: # Loop for all the user objects in the users array
      if user.username == self.username:
        return user # If the user exists, return the user object

  # Method to update the user's password
  def update_password(self):
    self.password = input("Please enter your password: ")

  # Method to check




users = []
storage_file = open('username_password.txt', 'r')
for line in storage_file:
  username, password = line.strip().split(',')
  users.append(user(username, password))

username = input('Please enter your username: ')
user = check_username(username, users)

if user is None:
    print('No such username found. Creating new account.')
    password = input('Please enter a new password: ')
    users.append(User(username, password))
    with open('username_password.txt', 'a') as file:
        file.write(f"{username},{password}\n")
else:
    for _ in range(5):
        password = input('Please enter your password: ')
        if password == user.password:
            print('Welcome!')
            break
        else:
            print('Wrong password. Please try again.')
    else:
        print('Wrong password entered 5 times. Application quit.')