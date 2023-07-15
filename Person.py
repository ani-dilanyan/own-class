from Date import Date
from datetime import date
from MyExceptions import PersonalDataTypeError, PersonalDataValueError, DateTypeError


# Create a new class Person
class Person:
    # Initialize data members if types and values given as arguments are valid,
    # otherwise raise corresponding errors
    def __init__(self, firstname, lastname, birthday: Date):
        try:
            # check whether the given value for firstname and lastname are strings
            if type(firstname) != str:
                raise PersonalDataTypeError("firstname", firstname)
            elif type(lastname) != str:
                raise PersonalDataTypeError("lastname", lastname)
            elif type(birthday) != Date:
                raise DateTypeError("birthday", birthday)

            # check whether the given value for birthday is valid and if so check the age to be greater than 18
            if not birthday.is_valid:
                raise PersonalDataValueError("Wrong value for birthday")
            else:
                if date.today().year - birthday.year < 18:
                    raise PersonalDataValueError("You must be at least 18 years old")
        except (PersonalDataValueError, PersonalDataTypeError, DateTypeError) as err:
            print(err)
        else:
            # if values and their types are valid initialise them to corresponding attributes
            self.firstname = firstname
            self.lastname = lastname
            self.birthday = birthday

    # Overwrite repr to return 'firstname' and 'lastname' attributes
    def __repr__(self):
        try:
            return "Firstname: {}\nLastname: {}".format(self.firstname, self.lastname)
        except AttributeError:
            return "Object is empty because of wrong initialisation"

# Initialisation tests

# p2 = Person("Firstname", "Lastname", Date(20, 2, 2000))
# p2 = Person("Firstname", "Lastname", Date(20, 20, 2000))
# p2 = Person("Firstname", "Lastname", Date(20, 2, 2006))

# print(p2)
