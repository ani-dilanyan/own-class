class DateValueError(Exception):
    def __init__(self, wrong_val_attribute, wrong_value):
        self.wrong_val_attribute = wrong_val_attribute
        self.wrong_value = wrong_value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.wrong_val_attribute, self.wrong_value)


class DateTypeError(Exception):
    def __init__(self, wrong_type_attribute, wrong_val):
        self.wrong_type_attribute = wrong_type_attribute
        self.wrong_val = wrong_val

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.wrong_type_attribute, type(self.wrong_val))


class MoneyTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


class MoneyValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class CustomerDataTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


# Creating new exception called CustomerDataValueError
class CustomerDataValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class TimeValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class TimeTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong type for {}: {}".format(self.message, type(self.value))


class TransactionTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


class TransactionValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Wrong value for {}: {}".format(self.message, self.value)


class RationalTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


class RationalValueError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class PersonalDataTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


class PersonalDataValueError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "{}".format(self.message)


class ProductTypeError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "Unsupported type for {}: {}".format(self.message, type(self.value))


class ProductValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

    def __str__(self):
        return "{}: {}".format(self.message, self.value)
