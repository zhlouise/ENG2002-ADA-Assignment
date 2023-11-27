class no_rat:
  def __init__(self, a, b): # Initialize the no_rat class
    rat = a/b  
    self.a = a
    self.b = b
    print ("The rational number you entered is {}/{}.".format(self.a, self.b))
  
  # Method for calculating the greatest common divisor between 2 integers. 
  def common_div(self, a, b):
    n = 0
    # Run a loop from 1 to the lowest number between a and b.
    for i in range(1, min(a, b) + 1):
      # For each loop, store the value of i into n 
      # if the remainder of a/i and b/i are both zero.
      if a % i == b % i == 0:
        n = i
    return n

  # Method that performs a division with another rational number
  # and returns the result as a rational number.
  def divide(self, other):
    # Dividing a/b by other_a/other_b
    new_a = self.a * other.b
    new_b = self.b * other.a
    # Dividing by gcd (greatest common divisor) to get the simplest form
    gcd = self.common_div(new_a, new_b)
    ans_a = int(new_a / gcd)
    ans_b = int(new_b / gcd)
    print("The rational answer for {}/{} divided by {}/{} is {}/{}."
          .format(self.a, self.b, other.a, other.b, ans_a, ans_b))
  
  # Method to calculate the nth power of a rational number
  def npower(self, n):
    # If the rational number is zero, raise a value error
    if self.a == 0: 
      raise ValueError
    else: 
      # Calculating the nth power of both numerator and denominator
      new_a = self.a ** n
      new_b = self.b ** n
      # Dividing by gcd (greatest common divisior) to get the simplest form
      gcd = self.common_div(new_a, new_b)
      ans_a = int(new_a / gcd)
      ans_b = int(new_b / gcd)
      print("The rational answer for {}/{} to the power of {} is {}/{}."
            .format(self.a, self.b, n, ans_a, ans_b))
    
    