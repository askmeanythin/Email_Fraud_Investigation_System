from utils.content_rule_loader import (
    ContentRuleLoader
)


class CredentialRequestDetector:

    def analyze(self, investigation):

        keywords = (
            ContentRuleLoader
            .load_credential_keywords()
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

        investigation.credential_request_analysis = (
            result
        )

        return investigation
    