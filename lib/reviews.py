class Review:
    reviews = []
    def __init__(self, customer,restaurant, rating):
        self.customer = customer
        self.restaurant_obj = restaurant
        self.rating = rating
        Review.reviews.append(self)

    def rating(self):
        return self.rating

    def get_rating(self):
        return self.rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant_obj 

    @classmethod
    def all(cls):
        return cls.reviews