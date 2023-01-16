
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        """Simple function that return the cost value of the shoe."""
        return self.cost

    def get_quantity(self):
        """Simple function that return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Constructor that returns a string representation of the Shoe class."""
        return f"Country: \t{self.country} \nCode: \t\t{self.code} \nProduct: \t{self.product} \
                \nCost ($): \t{self.cost} \nQuantity: \t{self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r", encoding="utf-8") as rfile:
            lines = rfile.readlines() 
            for index, line in enumerate(lines):
                # skips the first line of the inventory.txt file.
                if index == 0:
                    pass
                else:
                    # get each word of each line and add them 
                    # to their respectively variable
                    shoe_data = line.split(",")
                    for index, data in enumerate(shoe_data):
                        if index == 0:
                            country = data  # get the country of each product
                        elif index == 1:
                            code = data  # get the code of each product
                        elif index == 2:
                            product = data  # get the name of each product
                        elif index == 3:
                            cost = data  # get the code of each product
                        elif index == 4:
                            quantity = data  # get the quantity of each product
                    # create an instance of Shoe class and
                    # append it to the shoe_list list
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
    except Exception as error:
        print("Error:", error)
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    pass
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''