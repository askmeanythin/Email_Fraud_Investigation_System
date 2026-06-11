from utils.risk_rule_loader import (
    RiskRuleLoader
)


class RiskCalculator:

    def calculate(self, investigation):

        rules = (
            RiskRuleLoader.load_rules()
        )

        score = 0

        # Typosquatting
        if (
            investigation.typosquatting.get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "typosquatting",
                0
            )

        # Brand Impersonation
        if (
            investigation.brand_impersonation.get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "brand_impersonation",
                0
            )

        # Domain Age
        for data in (
            investigation.domain_age.values()
        ):

            age = data.get(
                "age_days"
            )

            if age is None:
                continue

            if age <= 7:

                score += rules.get(
                    "new_domain_7_days",
                    0
                )

            elif age <= 30:

                score += rules.get(
                    "new_domain_30_days",
                    0
                )

            elif age <= 90:

                score += rules.get(
                    "new_domain_90_days",
                    0
                )

        investigation.risk_score = score

        return investigation