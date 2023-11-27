# Create a class representing a customer of the application
class Customer:
  def __init__(self, username): # Initialize the customer class
      self.username = username
      self.password = '1234'


# Create text file 1234678.txt that contains the name, address, year of birth, and password '1234' in 4 lines.
txtfile = open('12345678.txt', 'w') # 'w' for writing into the file
txtfile.write('Chan Taiman\n76 Blandings, Sussex\n1976\n1234')
txtfile.close() # end the writing and close the file
# Continuously ask the user to input an account number until correctly entered
while True:
    account_num = input('Please enter the account number: ')
    if account_num == '12345678': 
        break # Break the loop if the account number is correctly entered.
    else:
        print('Wrong account number, please re-enter!')

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