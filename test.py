
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
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}".strip()

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

def view_all():
    read_shoes_data()
    for shoes in shoe_list:
        print(shoes)


    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python's tabulate module.
    '''

view_all()