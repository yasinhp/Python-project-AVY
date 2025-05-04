# data_processor.py
import pandas as pd
from models.real_estate import RealEstateProperty

class DataProcessor:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.preprocess()

    def preprocess(self):
        # Create derived column for price per sqft
        self.df["price_per_sqft"] = self.df["price"] / self.df["sqft_living"]
        # Drop rows with missing essential fields (if any)
        self.df.dropna(subset=["lat", "long", "price", "sqft_living", "zipcode"], inplace=True)

    def get_unique_zipcodes(self):
        return sorted(self.df["zipcode"].unique())

    def average_price_by_zipcode(self):
        return (
            self.df.groupby("zipcode")["price"]
            .mean()
            .reset_index()
            .sort_values("price", ascending=False)
        )