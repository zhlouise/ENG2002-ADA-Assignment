class no_rat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def common_div(self, a, b):
        n = 0
        for i in range(1, min(a, b) + 1):               #Method for calculating the greatest common divisor. Running a loop from 1 to the lowest number among a and b. Storing the value of i into n if remainder of a/i and b/i both are 0.
            if a % i == b % i == 0:
                n = i
        return n

    def divide(self, other_a, other_b):
        try:
            new_a = self.a * other_b  #Dividing a/b by other_a/other_b
            new_b = self.b * other_a
            gcd = self.common_div(new_a, new_b)
            print(f"{int(new_a / gcd)} / {int(new_b / gcd)}")  # Dividing by gcd to get the simplest form

        except:
            raise ValueError("Action not allowed: divisor = 0!")
