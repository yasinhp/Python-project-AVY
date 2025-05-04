# real_estate.py
class RealEstateProperty:
    def __init__(self, row):
        self.date = row['date']
        self.price = row['price']
        self.bedrooms = row['bedrooms']
        self.bathrooms = row['bathrooms']
        self.sqft_living = row['sqft_living']
        self.lat = row['lat']
        self.long = row['long']
        self.zipcode = row['zipcode']

    def price_per_sqft(self):
        return self.price / self.sqft_living if self.sqft_living > 0 else 0
