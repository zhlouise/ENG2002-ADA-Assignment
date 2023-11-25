# Function to display the main menu
def main_menu():
  # Loop to display main menu, where the user is repeatly asked to choose an operation
  while True: 
    print ("I: Input data")
    print ("Q: Quit\n")
    # Take user input for choice
    choice = input("Please enter your choice (I to input data and Q to quit): ")
    if choice == "I":
      input_data()  # Call input_data function
    elif choice == "Q":
      quit()  # Call quit function and break out of loop
      break
    else:
      # If user input is not one of the choices, prompt input again
      print ("Invalid input, please enter again!")

def input_data():
  while True:
    print ("a. Find the maximum")
    print ("b. Find the minimum")
    print ("c. Show the numbers in descending order")
    print ("d. Show the numbers in ascending order")
    print ("q. Return\n")
    sub_choice = input ("Please enter your choice (a, b, c, d, or q to return): ")
    if sub_choice == "a":
      print ("The maximum number is {}.".format(maximum()))
    elif sub_choice == "b":
      print ("The minimum number is {}.".format(minimum()))
    elif sub_choice == "c":
      print ("Numbers in descending order:")
      descending()
    elif sub_choice == "d":
      print("Numbers in ascending order: ")
      ascending ()
    elif sub_choice == "q":
      break
    else: 
      print ("Invalid input, enter again!")

def quit():
  print ("Goodbye!")


if __name__ == "__main__":
  main_menu()
