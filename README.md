# Restaurants--without-SQLAlchemy


![images](https://github.com/Arnold-Mwangi/Toy_Problems/assets/78974739/fb8447d9-1ba1-46b3-b42c-66ac408578b3)

## Code Challenge

This repository contains Restaurant solutions written in  Object Oriented Python. Each Solution focuses on OOP programming concepts and problem-solving techniques.

### Class 1: class Customer

#### Problem Statement
It includea a class attribute `all_custpomers`that holds all the customers that visit a certain restaurant
Also has some methods like:
        *`given_name`:  - returns the customer's given name
        *`family_name`: returns the customer's family name
        *`full_name`:   returns the full name of the customer, with the given name and the family name
        *`all`:   returns **all** of the customer instances
        
### class : Review
Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews

### class3: Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created


### OBJECT RELATIONSHIP METHODS
## Class: Review
- `Review customer()`
  - returns the customer object for that review
  - Once a review is created, should not be able to change the customer
- `Review restaurant()`
  - returns the restaurant object for that given review
  - Once a review is created, should not be able to change the restaurant

## Class Restaurant
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.


## Class Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
 
### Aggregate and Association Methods

  ## class Customer
    - `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored
- `Customer find_by_name(name)` class method
  - given a string of a **full name**, returns the **first customer** whose full name matches
- `Customer find_all_by_given_name(name)` class method
  - given a string of a given name, returns an **list** containing all customers with that given name
 
  ## Restaurant
    - `Restaurant average_star_rating()`
  - returns the average star rating for a restaurant based on its reviews
  - Reminder: you can calculate the average by adding up all the ratings and dividing by the number of ratings
  

## How to Run

1. Clone this repository to your local machine.
2. Navigate to the appropriate challenge directory.
3. Run pipenv install
4. Run the Python app.py script that has been used for testing all the classes.
6. The script will display the output based on the input provided.

Feel free to explore the code for each class, modify it as needed, and experiment with different inputs.

## Note

These solutions were developed as part of a coding exercise and may not cover all edge cases. They serve as examples of how to approach the given problems and may require further testing and refinement for production use.
