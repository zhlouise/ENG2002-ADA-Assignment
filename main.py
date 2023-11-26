import no_rat

# Function to display the main menu
def main_menu():
  # Loop to display main menu, where the user is repeatly asked to choose an operation
  while True: 
    # Print possible operation choices
    print ("D: Perform rational number division")
    print ("N: Compute nth power of rational numbers")
    print ("Q: Quit\n")
    # Take user input for choice
    choice = input("Please enter your choice (D, N, or Q to quit): ")
    if choice == "D":
      rat_div()  
    elif choice == "N":
      rat_npower()
    elif choice == "Q":
      quit()  # Call quit function and break out of loop (End application)
      break
    else:
      # If user input is not one of the choices, prompt input again
      print ("Invalid input, please enter again!")

# Function to perform division between 2 rational numbers that the user inputted
def rat_div():
  while True:
    # Ask the user to input the 2 rational numbers for performing the division
    a1 = int(input("Please enter the numerator of your first rational number: "))
    b1 = int(input("Please enter the denominator of your first rational number: "))
    # Make the rational numbers objects of class noRat
    rat_1 = no_rat(a1, b1)
    a2 = int(input("Please enter the numerator of your second rational number: "))
    b2 = int(input("Please enter the denominator of your second rational number: "))
    rat_2 = no_rat(a2, b2)

def rat_npower():
  print("holder")

def quit():
  print ("Goodbye!")


if __name__ == '__main__':
  main_menu()
