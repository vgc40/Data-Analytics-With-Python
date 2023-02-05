"""
    This file contains a combination of classes and funtions that store numbers and perform math
   
"""

class MyNumber:
    """
    This class is capable of saving a number and perfom other math opeations with it
    
    Attributes
    ----------
    x : integer
       Input number that the class stores

    Methods
    -------
    print():
        Print function to print the number    
    add(y):
        Performs a sum. It adds the number from a new input "y" to the number of this object, "x".
    subtract(y):
        Performs a substraction. It subtracts the number from a new input "y" to the number of this object, "x".
    main():
        Funtion with global variables to excecute the program if run in the command line

    """

    def __init__(self, x):
    """
    This function that instantiates classes into objects
    
    Parameters
    ----------
    self : 
       Variable always requiered in all functions in a class
     x: int
        Number that we want to store in the class
    Returns
    -------
    list
        object

    """
        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x

    def print(self):
    """
    This function prints new objects
    
    Parameters
    ----------
    self : 
       Variable always requiered in all functions in a class
     x: int
        Number that we want to store
    Returns
    -------
    list
        Print new class object

    """
        print("The number is: {}".format(self.x))

    def add(self, y):
    """
    This function that adds an integer to an object
    
    Parameters
    ----------
    self : 
       Variable always requiered in all functions in a class
    y: int
        Number that we want to add
    Returns
    -------
    list
        Print result of the mathematical operation addition

    """
        self.x = self.x + y

    def subtract(self, y):
     """
    This function that subtracts an integer to an object
    
    Parameters
    ----------
    self : 
       Variable always requiered in all functions in a class
    y: int
        Number that we want to subtract
    Returns
    -------
    list
        Print result of the mathematical operation subtraction

    """
        self.x = self.x - y


def main():
    """
    This function contains global variables to run the program when running from command-line
    
    Parameters
    ----------
    None
  
    Returns
    -------
    list
        Prints the object as well as the result of the mathematical operation addition/subtraction of the number 2

    """
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

if __name__ == "__main__":
    main()