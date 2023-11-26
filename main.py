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
      quit()  # Call quit function and break out of loop
      break
    else:
      # If user input is not one of the choices, prompt input again
      print ("Invalid input, please enter again!")

# Function to perform division between 2 rational numbers that the user inputted
def rat_div():
  while True:
    
    print ("q. Return\n")
    

def rat_npower():
  

def quit():
  print ("Goodbye!")


if __name__ == "__main__":
  main_menu()
