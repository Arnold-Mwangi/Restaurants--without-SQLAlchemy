from customer import Customer
from restaurant import Restaurant
from reviews import Review

# Creating customers
arnold = Customer('Arnold', 'Mwangi')
harriet = Customer('Harriet', 'Koech')

# Creating restaurants
restaurant1 = Restaurant('Restaurant One')
restaurant2 = Restaurant('Restaurant Two')

# Adding reviews
arnold.add_review(restaurant1, 4)
arnold.add_review(restaurant2, 5)
harriet.add_review(restaurant1, 3)

# Testing additional methods
print(f"{arnold.full_name()} has authored {arnold.num_reviews()} reviews.")
print(f"Average rating for {restaurant1.get_name()}: {restaurant1.average_star_rating()}")

print("Customers who reviewed Restaurant One:")
for customer in restaurant1.customers():
    print(customer.full_name())

print("Restaurants reviewed by Arnold:")
for restaurant in arnold.restaurants():
    print(restaurant.get_name())

# Finding customers by name
found_customer = Customer.find_by_name('Arnold Mwangi')
if found_customer:
    print(f"Found customer: {found_customer.full_name()}")

# Finding all customers with a given name
given_name_customers = Customer.find_all_by_given_name('Harriet')
if given_name_customers:
    print("Customers with given name 'Harriet':")
    for customer in given_name_customers:
        print(customer.full_name())
