
#========The beginning of the class==========
class Shoe:
    """
    Class that has the objective to create a shoe object for XX Store.

    Attributes
    ----------
    country : str
        The country which the shoe is located.
    code : str
        The unique ID code number of the shoe.
    product : str
        The name of the shoe.
    cost : str
        The price number cost of the shoe.
    quantity: str
        The quantity number of the shoe currently in stock.

    Methods
    -------
    get_cost()
        Returns the cost value of the shoe.
    get_quantity()
        Returns the currently quantity value in stock of the shoe.
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Constructos all the necessary attributes for the shoe object.

        Parameters
        ----------
            country : str
                The country which the shoe is located.
            code : str
                The unique ID code number of the shoe.
            product : str
                The name of the shoe.
            cost : str
                The price number cost of the shoe.
            quantity: str
                The quantity number of the shoe currently in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
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
    """Function that opens inventory.txt file, read the data stored inside it to use them to create a shoes object which will be appended into the shoe_list list."""
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

def capture_shoes():
    """Function that creates a new shoes objects by getting five inputs from user. Append this new object into inventory.txt file.
    Print out on screen message saying that the new shoe was registered.
    """
    #  Inputs thhat will be used to create the new shoe object
    #  try-except-else block to get the correct values for each data.
    while True:
        print(f"\n{'REGISTER NEW SHOE':^50s}")
        print(f"{'-' * 50}")    
        try:
            country_of_shoe_input = input("\nCountry: \t").strip().capitalize()
            if not country_of_shoe_input:
                raise ValueError("Empty field. \nPlease enter the name of the country. \nEx.: England")
   
            code_of_shoe_input = input("Code: \t\t").strip().upper()
            #  Condition to get the code exactly on this format: SKUNNNNN; where N == number.
            if (not code_of_shoe_input or
                len(code_of_shoe_input) != 8 or
                code_of_shoe_input[:3] != "SKU" or
                not code_of_shoe_input[3:].isdigit()):
                raise ValueError("Empty field. \nPlease enter the code of the shoe. \nEx.: SKU00000")

            product_of_shoe_input = input("Product: \t").strip().title()
            if not product_of_shoe_input:
                raise ValueError("Empty field. \nPlease enter the name of the shoe. \nEx.: Nike Air Max 200")
        except ValueError as error:
            print("\nERROR:", error)
        else:
            try:
                cost_of_shoe_input = int(input("Cost: \t\t").strip())
                quantity_of_shoe_input = int(input("Quantity: \t").strip())
                break
            except ValueError as error:
                print("\nError:", error)
        
    #  Create new shoe object that will be appended on the inventory.txt file.
    new_shoe_object = Shoe(
        country_of_shoe_input, 
        code_of_shoe_input, 
        product_of_shoe_input, 
        cost_of_shoe_input, 
        quantity_of_shoe_input
    )

    #  try-except-else block to check if the file whether is correct or not.
    try:
        with open("inventory.txt", "a") as afile:
            afile.write(f"\n{new_shoe_object.country},{new_shoe_object.code},{new_shoe_object.product},{new_shoe_object.cost},{new_shoe_object.quantity}")
    except FileNotFoundError as error:
        print("ERROR:", error)
    else:
        print(f"\n{'-' * 50}")
        print(f"\n{'NEW SHOE REGISTERED!':^50s}\n")

def view_all():
    """Simple function that print out all shoes' contents inside inventore.txt file according to its __str__ magic function."""
    #  Check whether shoe_list list it empty or not.
    #  If it is not empty; print out its data.
    #  If it is empty; print out message saying this information.
    if shoe_list:
        print(f"\n{'LIST OF ALL SHOES AVAILABLES':^50s}")
        print("")
        for shoe in shoe_list:
            print(shoe)
        print(f"{'-' * 50}")
        print("")
        print(f"{'END':^50s}")
    else:
        print(f"\n{'LIST OF ALL SHOES AVAILABLES':^50s}")
        print("")
        print(f"{'<NONE> : EMPTY LIST':^50s}")
        print("")
        print(f"{'END':^50s}")

def re_stock():
    """Function that get the shoe object with the lowest quantity in stock and ask to user if wants to increase the currently number of stock level."""
    global shoe_list
    quantity_of_shoe_list = []  # list that will receive all quantity numbers of each shoes inside the shoe_list.
    
    #  Check if shoe_list list is empty; If yes, print out message that says it to user.
    #  Otherwise; proceed to execute rest of the function.
    if not shoe_list:
        print(f"\n{'SHOE LOWEST STOCK':^50s}")
        print("")
        print(f"{'<NONE> : EMPTY LIST':^50s}")
        print("")
        print(f"{'END':^50s}")
    else:
        #  gets numbers all quantity of each shoes.
        for shoe in shoe_list:
            quantity_of_shoe_list.append(int(shoe.quantity.strip()))

        #  get the index from minimum quantity number of the list
        #  in order to locate the object on shoe_list.
        min_quantity_shoe_index = 0
        for index, number_shoe_list in enumerate(quantity_of_shoe_list):
            if number_shoe_list == min(quantity_of_shoe_list):
                min_quantity_shoe_index = index
                break

        #  Display all relevant data about the shoe with
        #  the lowest quantity in stock on screen by using
        #  for-loop and comparing the index of shoe_list list
        #  with the number of the min_quantity_shoe_index.
        print(f"{'SHOE LOWEST STOCK':^37s}")
        for index, shoe in enumerate(shoe_list):
            #  Continue if is not the shoe that we want.
            if index != min_quantity_shoe_index:
                pass
            else:
                print(shoe)

                #  ask user if wants to increase this number.
                #  if yes, proceed with the operation.
                #  Otherwise, leave the program
                while True:
                    user_input = input("\nWould like to increase the currently \nstock level of this product (y/n)? ").strip().lower()
                    if user_input == "y":
                        try:
                            new_quantity = input("\nEnter new number of stock: ")  # new quantity number.
                            shoe.quantity = new_quantity  #  change the quantity of the object which is inside shoe_list.
        
                            #  Display message saying the stock has been updated.
                            print(f"\n{'SHOE STOCK UPDATED:':^37s}")
                            print(shoe)
                            #  Here, we are going to modify the specific line that has been updated
                            #  inside the inventory.txt file.
                            #  First, we open the file to grab all the lines inside there.
                            try:
                                with open("inventory.txt", "r", encoding="utf-8") as rfile:
                                    get_all_lines = rfile.readlines()
                            except FileNotFoundError as error:
                                print("ERROR:", error)

                            #  Finally, open the file again to change the content that the user wants to.
                            try:
                                with open("inventory.txt", "w") as wfile:
                                    for index, line in enumerate(get_all_lines):
                                        #  Check if the index of the line mathces with the one that we get
                                        #  from the list which has all quantity numbers.
                                        #  If matches, then update the line with the new value.
                                        #  Otherwise, just write the same line againn.
                                        if index - 1 == min_quantity_shoe_index:
                                            wfile.writelines(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n") 
                                        else:
                                            wfile.writelines(line)
                            except FileNotFoundError as error:
                                print("ERROR:", error)

                            shoe_list = []  #  Clear the shoe_list in order to not duplicate its values
                            break
                        except Exception as error:
                            print("Error:", error)
                    elif user_input == "n":
                        break
                    else:
                        print("\nInvalid Option! Try again later!")

def search_shoe(code):
    """Simple function that return the shoe object according to its unique code number.
    
    Parameters
    ----------
        code : str
            Unique code number of the item shoe.
    
    Returns
    -------
        shoe : obj
            shoe object from the shoe_list list.
        f-string message : str
            error message that says the code was not found in the shoe_list list.
    """
    is_shoe_code = False  #  Control variable to determine whether the code was found in the shoe_list list or not.  
    for shoe in shoe_list:
        if code == shoe.code:  #  Get the shoe according to its unique code.
            is_shoe_code = True
            return shoe  #  Return the shoe object.
    
    #  Return error message if code is not in the shoe_list list.
    if not is_shoe_code:
        return (f"\nError: {code} not found! \nPlease, check to see if you entered the correct code!")

def value_per_item():
    """Function that print out to user the total value of each item by using the following formula: cost * quantity."""
    # If shoe_list list is not empty; print out the data.
    if shoe_list:
        print(f"{'TOTAL VALUE OF EACH SHOE':^50s}")
        print(f"{'-' * 50}")
        for shoe in shoe_list:
            total_value = float(shoe.cost) * int(shoe.quantity)
            print(f"{shoe.product:^20s} \t- \t£{total_value:,.2f}.")
    
    #  Otherwise; print out empty list message.
    else:
        print(f"\n{'TOTAL VALUE OF EACH SHOE':^50s}")
        print("")
        print(f"{'<NONE> : EMPTY LIST':^50s}")
        print("")
        print(f"{'END':^50s}")

def highest_qty():
    """Function that get the shoe with the highest number of stock and print out message saying like it was for sale."""
    #  Check if shoe_list list is empty or not.
    #  If not; execute the function.
    #  If it is; print out empty list message.
    if shoe_list:
        quantity_of_shoe_list = []  #  variable that will receive all value
        for shoe in shoe_list:
            quantity_of_shoe_list.append(int(shoe.quantity.strip()))  #  Get all quantities of each shoe; Store it into a new list.
        
        max_quantity_shoe_index = 0
        for index, number_quantity_shoe_list in enumerate(quantity_of_shoe_list):
            if number_quantity_shoe_list == max(quantity_of_shoe_list):
                max_quantity_shoe_index = index  #  Get the index of the highest number in quantity_of_shoe_list list.

        for index, shoe in enumerate(shoe_list):
            #  Get the shoe with the highest number of stock and
            #  print out on screen its data as it was for sale.
            if index == max_quantity_shoe_index:
                print(f"{'WONDERFUL SHOE FOR SALE':^50s}")
                print(f"{'-' * 50}")
                print(f"{shoe.product.strip().title()} for only £{shoe.cost.strip()},00.\nDo not loose this opportunity!")
                print(f"Offer available only in {shoe.country.title()}.")

    else:
        print(f"\n{'WONDERFUL SHOE FOR SALE':^50s}")
        print("")
        print(f"{'<NONE> : EMPTY LIST':^50s}")
        print("")
        print(f"{'END':^50s}")


#==========Main Menu=============
#  Menu that only will stop after user press button 7.
while True:
    #  First-thing-first is to check whether our main file inventory.txt 
    #  was found or not. If yes, proceed to the rest of the program.
    #  Otherwise; print out error message and do not execute the program.
    try:
        read_shoes_data()  #  Initialize shoe_list list.
    
    except FileNotFoundError as error:
        print("ERROR:", error)
        break
    
    else:
        print(f"{'-' * 60}")
        #  try-except-else block to make sure user entered integer number
        try:
            menu = int(input("""Please choose one of the options below:
[1] To view all shoe in stock
[2] To get the lowest shoe in stock that need be re-stocked
[3] To view the highest shoe in stock
[4] To see the total value of each shoe in stock
[5] To register a new shoe in stock
[6] To search a specific shoe in stock by its unique code number
[7] To exit the program

-> """))
        except ValueError as error:
            print("\nERROR:", error, "\n")
        else:
            #  Exit the program
            if menu == 7:
                print(f"{'-' * 50}")
                print(f"{'Good-Bye!':^50s}")
                exit()
            
            #  View all shoes in stock
            elif menu == 1:
                view_all()
            
            #  Get lowest shoe in stock and ask user if
            #  wants to re-stock it or not
            elif menu == 2:
                re_stock()
            
            #  View highest shoe in stock
            elif menu == 3:
                highest_qty()
            
            #  See total value of each item on screen
            elif menu == 4:
                value_per_item()

            #   Register a new shoe 
            elif menu == 5:
                capture_shoes()

            #  Search specific shoe by its own code
            elif menu == 6:
                try:
                    wanted_shoe_code = input("\nEnter the code of the shoe you wanted to find: ").upper().strip()
                    wanted_shoe = search_shoe(wanted_shoe_code)
                    print(wanted_shoe)
                except Exception as error:
                    print("Error:", error)
            else:
                print("\nInvalid Option! \nPlease, choose an option between 1 - 7.\n")