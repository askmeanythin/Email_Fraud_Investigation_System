import json


class BrandLoader:

    @staticmethod
    def load_brands():

        with open(
            "data/brand_database/trusted_brands.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)