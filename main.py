import no_rat


# Function to display the main menu
def main_menu():
  # Loop to display main menu, where the user is repeatly asked to choose an operation
  while True: 
    # Print possible operation choices
    print ("D: Perform rational number division")
    print ("N: Compute nth power of rational numbers")
    print ("Q: Quit")
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
    # Ask the user to input a rational number for performing the division
    try:
      a1 = int(input("Please enter the numerator of your first rational number (integer only): "))
      b1 = int(input("Please enter the denominator of your first rational number (integer only): "))
    # If the input is not an integer, ask the user to re-input
    except ValueError:
      print("Invalid integer input, please try again.")
      continue
    # Make the rational number into an object of class no_rat
    try: 
      rat_1 = no_rat.no_rat(a1, b1)
    # If the denominator is zero, display an error message and ask the user to re-input.
    except ZeroDivisionError:
      print("Action not allowed: cannot divide by zero! Try again.")
      # If an error is raised, skip the entire iteration
      # and ask the user to key in the rational numbers again.
      continue
    
    # Repeat for the second rational number
    try: 
      a2 = int(input("Please enter the numerator of your second rational number (integer only): "))
      b2 = int(input("Please enter the denominator of your second rational number (integer only): "))
    except ValueError:
      print("Invalid integer input, please try again.")
      continue
    try:
      rat_2 = no_rat.no_rat(a2, b2)
    except ZeroDivisionError:
      print("Action not allowed: cannot divide by zero! Try again.")
      continue
      
    # Calculate the ratio between the 2 rational numbers using the method in no_rat
    try: 
      rat_1.divide(rat_2)
    except ZeroDivisionError: # If the denominator is zero, then raise a value error
      print("Action not allowed: cannot divide by zero! Try again.")
      continue
     
    while True:
      # Prompt the user to quit this operation or to continue another operation
      rt_choice = input("Input R to return to main menu, or C to continue another calculation: ")
      if rt_choice == "R":
        return
      elif rt_choice == "C":
        break
      else:
        # If user input is not one of the choices, prompt input again
        print ("Invalid input, please enter again!")


def rat_npower():
  print("holder")


def quit():
  print ("Goodbye!")


if __name__ == '__main__':
  main_menu()
