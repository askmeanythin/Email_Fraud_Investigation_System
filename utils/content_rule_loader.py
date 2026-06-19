import json


class ContentRuleLoader:

    @staticmethod
    def load_urgency_keywords():

        with open(
            "data/content_rules/urgency_keywords.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
        
    @staticmethod
    def load_credential_keywords():

        with open(
            "data/content_rules/credential_keywords.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
        
    @staticmethod
    def load_financial_keywords():

        with open(
            "data/content_rules/financial_keywords.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)