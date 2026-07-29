class NumberUtility:
    
    def __init__(self , number):
        self.number = number 
        
    def is_even(self):
        """
        this function checks whether the number is even or odd.

        Returns:
            bool: True if the number is even, False if it is odd.
        """
        return self.number % 2 == 0
    def check_sign(self):
        """ 
        this function checks the sign of the number.
        
        Returns:
            str: A string indicating whether the number is positive, negative, or zero.
        """
        if self.number > 0 :
            return "positive"
        elif self.number < 0 :
            return "negative"
        else:
            return "zero"
    
    def is_leap_year(self):
        """
        this function checks whether the number is a leap year.

        Returns:
            bool: True if the number is a leap year, False otherwise.
        """
        
        if self.number % 400 == 0 :
            return True
        elif self.number % 100 == 0 :
            return False
        elif self.number % 4 == 0 :
            return True
        else :
            return False
    
    

