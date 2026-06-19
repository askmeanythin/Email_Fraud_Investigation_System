import json


class TLDLoader:

    @staticmethod
    def load_tlds():

        with open(
            "data/suspicious_tlds/tlds.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)