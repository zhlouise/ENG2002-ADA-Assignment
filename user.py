# Create a class representing a customer of the application
class Customer:
  def __init__(self, username): # Initialize the customer class
    self.username = username
    self.password = '1234'


# Create text file 1234678.txt that contains the name, address, year of birth, and password '1234' in 4 lines.
txtfile = open("username_password.txt", 'w') # 'w' for writing into the file
txtfile.write("Username: {}/nPassword: {}/n".format(username, password))
txtfile.close() # end the writing and close the file
# Ask the user to input their username
username = input('Please enter your username: ')

for i in range(5): # Allow the user to key in the password for a maximum of 5 times
    if account_num == '12345678': 
      break # Break the loop if the account number is correctly entered.
    else:
      print('Wrong password, please re-enter!')
      if i == 4: # 
        print("Wrong password entered 5 times, application quitted.")

# After the correct account number is entered, read input args from the txtfile
txtfile = open('12345678.txt', 'r')
customer_name = txtfile.readline().rstrip('\n') #Remove the '\n' at the end of the string
customer_address = txtfile.readline().rstrip('\n')
customer_yob = int(txtfile.readline().rstrip('\n')) # Also convert the yob from string type to integer type
txtfile.close() # Close the file

# Instantiate a BankAccount and a Customer object
customer = Customer(customer_name, customer_address, customer_yob)
account = BankAccount(customer, 12345678)

# Ask the user to key in the password until the correct password is entered
while True:
    pw = input('Enter the password: ')
    if pw == '1234':
        break
    else:
        print('Wrong password, please re-enter!') 

# Once the correct pw is entered, prompt the user to change password.
print('You need to change your password')
# Ask the user to key in new password twice until they match
while True:
    new_pw_1 = input('Enter new password: ')
    new_pw_2 = input('Re-enter the new password: ')
    if new_pw_1 == new_pw_2:
        break
    else:
        print('Not matching, please enter password again!')

# Display the new password
print('Your new password is {}'.format(new_pw_1))

# Update the user password in the Customer object
customer.password = new_pw_1

# Update the user password in the txtfile
txtfile = open('12345678.txt','r') # 'r' for reading the file
txtfile_string = txtfile.read() # Read txtfile as a string
txtfile.close() # Close the txtfile
txtfile = open('12345678.txt', 'w') # 'w' for re-writing the file
txtfile.write(txtfile_string.replace('1234',customer.password)) # Replace old password in original string
txtfile.close() # Close the txtfile


# Create a class representing a user of the application
class user:
    def __init__(self, username, password): # Initialize a user object with UN and PW
        self.username = username
        self.password = password

  # Method to check whether a user already exists or not
  def check_username(username, users): # Note: users is an array of all the registered users of this application
    for user in users: # Loop for all the user objects in the users array
      if user.username == username:
        return user # If the user exists, return the user object

  def update_password(username, password, users):
    for user in users:
      if user.username == username:
        user.password = password

def main():
    users = []
    with open('username_password.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            users.append(User(username, password))

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

if __name__ == '__main__':
    main()