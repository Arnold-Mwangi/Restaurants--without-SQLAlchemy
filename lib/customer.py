class Customer:

    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def _all_customers(cls):
        return cls.all_customers

    def set_given_name(self, new_g_name):
        self.given_name = new_g_name

    def set_f_name(self, new_f_name):
        self.family_name = new_f_name

    @classmethod
    def print_all_customers(cls):
        if cls.all_customers:
            for customer in cls.all_customers:
                print(customer.full_name())
        else:
            print("No customers yet")

# tests

cus1 = Customer('Arnold', 'Mwangi')
cus3 = Customer('Harriet', 'Koech')

print(cus1.full_name())

print(Customer.print_all_customers())
