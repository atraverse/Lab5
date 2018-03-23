class Property:
    """ Return the dictionary with the entered data """
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        super().init(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        (None)->(none)
        Print to console some information
        """
        print("PROPERTY DETAILS")
        print("================")
        print("Square footage: {}".format(self.square_feet))
        print("Bedrooms: {}".format(self.num_bedrooms))
        print("Bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        (none)->(dict)
        Return dictionary
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """ Return and update dictionary with the entered data """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().init(**kwargs)#inheritance method
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        (None)->(none)
        Print to console some information
        """
        super().display()#inheritance Property method
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        (None)->(dict)
        Return dict with getted data about laundry and balcony from user
        """
        parent_init = Property.prompt_init() #composition Property method
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
            balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? "
                "({})".format(", ".join(Apartment.valid_balconies)))

        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    (str, str)->(str)
    Return result of input
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


def prompt_init():
    """
    (None) -> (dict)
    Call some function for input of classes (PROPERTY/APARTMENT)
    """
    parent_init = Property.prompt_init()
    laundry = get_valid_input(
        "What laundry facilities does "
        "the property have? ",
        Apartment.valid_laundries)
    balcony = get_valid_input(
        "Does the property have a balcony? ",
        Apartment.valid_balconies)
    parent_init.update({
        "laundry": laundry,
        "balcony": balcony
    })
    return parent_init


prompt_init = staticmethod(prompt_init)


class House(Property):
    """ Return and update dictionary with the entered data """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")


    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().init(**kwargs)#inheritance method
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories


    def display(self):
        """
        (None)->(none)
        Print to console some information
        """
        super().display()#inheritance Property method
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        (None)->(dict)
        Call some function for input of classes (PROPERTY/APARTMENT)
        """
        parent_init = Property.prompt_init()#composition Property method
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)

        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """ Return dictionary with the entered data """
    def __init__(self, price='', taxes='', **kwargs):
        super().init(**kwargs)#inheritance method
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        (None)->(none)
        Print to console some information
        """
        super().display()#inheritance Property method
        print("PURCHASE DETAILS")

        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """ Return dictionary with the entered data """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().init(**kwargs)#inheritance method
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        (None)->(none)
        Print to console some information
        """
        super().display()#inheritance Property method
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        (None)->(dict)
        Rerturn dict with infromation that was getting from console
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """ Return and update dictionary with the entered data """
    def prompt_init():
        """
        (None)->(dict)
        Call some function for input of classes (House)
        """
        init = House.prompt_init()#composition House method
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """ Return and update dictionary with the entered data """
    def prompt_init():
        """
        (None)->(dict)
        Call some function for input of classes (APARTMENT)
        """
        init = Apartment.prompt_init()#composition Apartment's method
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """ Return and update dictionary with the entered data """
    def prompt_init():
        """
        (None)->(dict)
        Call some function for input of classes (APARTMENT)
        """
        init = Apartment.prompt_init()#composition Apartment's method
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """ Return and update dictionary with the entered data """
    def prompt_init():
        """
        (None)->(dict)
        Call some function for input of classes (HOUSE)
        """
        init = House.prompt_init()#composition House's method
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """Main class for all another classes"""
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        (None)->(none)
        Print to console some information
        """
        for property in self.property_list:
            property.display()

    type_map = {
           ("house", "rental"): HouseRental,
           ("house", "purchase"): HousePurchase,
           ("apartment", "rental"): ApartmentRental,
           ("apartment", "purchase"): ApartmentPurchase
           }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
