from utils.content_rule_loader import (
    ContentRuleLoader
)


class FinancialScamDetector:

    def analyze(self, investigation):

        keywords = (
            ContentRuleLoader
            .load_financial_keywords()
        )

        body = (
            investigation.plain_text_body
            .lower()
        )

        detected_keywords = []

        for keyword in keywords:

            if keyword.lower() in body:

                detected_keywords.append(
                    keyword
                )

        result = {
            "detected": (
                len(
                    detected_keywords
                ) > 0
            ),
            "keywords": (
                detected_keywords
            )
        }

        investigation.financial_scam_analysis = (
            result
        )

        return investigation