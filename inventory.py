
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
        return f"{'-' * 37} \n {'Country:':>11s} {' ' * 4} {self.country:<15s} \n{'Code:':>12s} {' ' * 4} \
{self.code:<15s} \n {'Product:':>11s} {' ' * 4} {self.product:<20s} \n {'Cost ($):':>11s} {' ' * 4} {self.cost:<10s}\
 \n {'Quantity:':>11s} {' ' * 4} {self.quantity}".strip()

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
    #  Inputs thhat will be used to create the new shoe object
    country_of_shoe_input = input("Country: ")
    code_of_shoe_input = input("Code: ")
    product_of_shoe_input = input("Product: ")
    cost_of_shoe_input = int(input("Cost: "))
    quantity_of_shoe_input = int(input("Quantity: "))

    new_shoe_object = Shoe(
        country_of_shoe_input, 
        code_of_shoe_input, 
        product_of_shoe_input, 
        cost_of_shoe_input, 
        quantity_of_shoe_input
    )

    with open("inventory.txt", "a") as afile:
        afile.write(f"\n{new_shoe_object.country},{new_shoe_object.code},{new_shoe_object.product},{new_shoe_object.cost},{new_shoe_object.quantity}")
    '''
    LOGIC IS PRETTY MUCH DONE - NEED TO REVISE ERROR HANDLING AND OUTPUT FORMATTING!!!
    '''

def view_all():
    """Simple functoion that print out all shoes' contents inside inventore.txt file according to its __str__ magic function."""
    try:
        read_shoes_data()  #  Initialize shoe_list.
        print(f"{'LIST OF ALL SHOES AVAILABLES':^37s}")
        print("")
        for shoe in shoe_list:
            print(shoe)
        print(f"{'-' * 37}")
        print("")
        print(f"{'END':^37s}")
    except Exception as error:
        print("Error:", error)

def re_stock():
    quantity_of_shoe_list = []  # list that will receive all quantity numbers of each shoes inside the shoe_list.
    read_shoes_data()
    #  gets numbers all quantity of each shoes
    for shoe in shoe_list:
        quantity_of_shoe_list.append(int(shoe.quantity.strip()))
    
    #  get the index from minimum quantity number of the list
    #  in order to locate the object on shoe_list
    min_quantity_shoe_index = 0
    for index, number_shoe_list in enumerate(quantity_of_shoe_list):
        if number_shoe_list == min(quantity_of_shoe_list):
            min_quantity_shoe_index = index
            break
    
    #  Display all relevant data about the shoe with
    #  the lowest quantity in stock on screen.
    print(f"{'SHOE LOWEST STOCK':^37s}")
    for index, shoe in enumerate(shoe_list):
        if index == min_quantity_shoe_index:
            print(shoe)

            #  ask user if wants to increase this number.
            #  if yes, proceed with the operation.
            #  Otherwise, leave the program
            while True:
                user_input = input("\nWould like to increase the currently \nstock level of this product (y/n)? ").strip().lower()
                if user_input == "y":
                    try:
                        new_quantity = int(input("\nEnter new number of stock: "))  # new quantity number.
                        shoe.quantity = new_quantity  #  change the quantity of the object which is inside shoe_list.
                        new_shoe = shoe  #  grab this object in order to change the contents inside inventory.txt later.
                        
                        #  Display message saying the stock has been updated.
                        print(f"\n{'SHOE STOCK UPDATED:':^37s}")
                        print(shoe)
                        #  Here, we are going to modify the specific line that has been updated
                        #  inside the inventory.txt file.
                        #  First, we open the file to grab all the lines inside there.
                        with open("inventory.txt", "r", encoding="utf-8") as rfile:
                            get_all_lines = rfile.readlines() 

                        #  Finally, open the file again to change the content that the user wants to.
                        with open("inventory.txt", "w") as wfile:
                            for index, line in enumerate(get_all_lines):
                                #  Check if the index of the line mathces with the one that we get
                                #  from the list which has all quantity numbers.
                                #  If matches, then update the line with the new value.
                                #  Otherwise, just write the same line againn.
                                if index - 1 == min_quantity_shoe_index:
                                    wfile.writelines(f"{new_shoe.country}, {new_shoe.code}, {new_shoe.product}, {new_shoe.cost}, {new_shoe.quantity}\n") 
                                else:
                                    wfile.writelines(line)
                        break
                    except Exception as error:
                        print("Error:", error)
                elif user_input == "n":
                    print("\nGoodbye!")
                    break
                else:
                    print("\nInvalid Option! Try again later!")
    '''
    LOGIC IS PRETTY MUCH DONE!!! JUST NEED TO REVISE ERROR HANDLING!!!!
    '''

def search_shoe(code):
    """Simple function that return the shoe object according to its unique code number."""
    read_shoes_data()  #  Initialize shoe_list.
    for shoe in shoe_list:
        if code == shoe.code:  #  Get the shoe according to its unique code.
            return shoe  #  Return the shoe object.
    '''
    LOGIC IS PRETTY MUCH DONE! NEED TO REVISA ERROR HANDLING!
    '''

def value_per_item():
    read_shoes_data()
    print(f"{'TOTAL VALUE OF EACH SHOE':^50s}")
    print(f"{'-' * 50}")
    for shoe in shoe_list:
        total_value = float(shoe.cost) * int(shoe.quantity)
        print(f"\n{shoe.product:^20s} \t- \t£{total_value:,.2f}.")
    '''
    LOGIC IS PRETTY MUCH DONE - NEED TO REVISE ERROR HANDLING!!!!
    '''

def highest_qty():
    read_shoes_data()  #  Initialize shoe_list.
    quantity_of_shoe_list = []  #  variable that will receive all value
    for shoe in shoe_list:
        quantity_of_shoe_list.append(int(shoe.quantity.strip()))
    
    max_quantity_shoe_index = 0
    for index, number_quantity_shoe_list in enumerate(quantity_of_shoe_list):
        if number_quantity_shoe_list == max(quantity_of_shoe_list):
            max_quantity_shoe_index = index

    for index, shoe in enumerate(shoe_list):
        if index == max_quantity_shoe_index:
            print(f"{'Wonderful Shoe For Sale':^50s}")
            print(f"{'-' * 50}")
            print(f"{shoe.product.strip().title()} for only £{shoe.cost.strip()},00.\nDo not loose this opportunity!")
            print(f"Offer available only in {shoe.country.title()}.")
    '''
    LOGIC IS PRETTY MUCH DONE! NEED TO REVISE ERROR HANDLING!
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
#  Menu that only will stop after user press button 7.
while True