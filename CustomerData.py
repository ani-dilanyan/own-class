from Person import Person
from MyExceptions import CustomerDataTypeError, CustomerDataValueError


class CustomerData(Person):
    def __init__(self, firstname, lastname, birthday, email, password, phone_number, passport_number):
        super().__init__(firstname, lastname, birthday)
        try:
            if type(email) != str:
                raise CustomerDataTypeError("email", email)
            elif type(password) != str:
                raise CustomerDataTypeError("password", password)
            elif type(phone_number) != str:
                raise CustomerDataTypeError("phone number", phone_number)
            elif type(passport_number) != str:
                raise CustomerDataTypeError("Passport number", passport_number)

            if len(password) < 8:
                raise CustomerDataValueError("Password. Password must contain at least 8 characters", password)
            elif len(phone_number) < 8:
                raise CustomerDataValueError("Phone number. Must contain 8 characters after after country code",
                                             phone_number)
        except (CustomerDataValueError, CustomerDataTypeError) as err:
            print(err)
        else:
            self.email = email
            self.__password = password
            self.phone_number = phone_number
            self.__passport_number = passport_number

    def __repr__(self):
        try:
            return "Client name: {} {}\nE-mail: {}\nPhone number: {}\n".format(self.firstname, self.lastname,
                                                                               self.email, self.phone_number)
        except AttributeError:
            return "Object is empty. Account setup is incomplete"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

# c = Customer("Firstname", "Lastname", Date(20, 2, 2000), "example@gmail.com", "password", "99999999", "AV0000000")
#
# print(c)
