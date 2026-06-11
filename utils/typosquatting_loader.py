import json


class TyposquattingLoader:

    @staticmethod
    def load_replacements():

        with open(
            "data/typosquatting/replacements.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @staticmethod
    def load_suspicious_words():

        with open(
            "data/typosquatting/suspicious_words.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)