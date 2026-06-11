import json


class RiskRuleLoader:

    @staticmethod
    def load_rules():

        with open(
            "data/risk_rules/scoring_rules.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)