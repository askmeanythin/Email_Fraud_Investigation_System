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


        # IP URL Detection
        if (
            investigation.url_analysis
            .get(
                "ip_url",
                {}
            )
            .get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "ip_url_detected",
                0
            )

        # Suspicious TLD
        if (
            investigation.url_analysis
            .get(
                "suspicious_tld",
                {}
            )
            .get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "suspicious_tld",
                0
            )    

        # SPF
        if (
            investigation.spf_analysis
            .get("result")
            == "fail"
        ):
            score += rules.get(
                "spf_fail",
                0
            )

        # DKIM
        if (
            investigation.dkim_analysis
            .get("result")
            == "fail"
        ):
            score += rules.get(
                "dkim_fail",
                0
            )

        # DMARC
        if (
            investigation.dmarc_analysis
            .get("result")
            == "fail"
        ):
            score += rules.get(
                "dmarc_fail",
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

        # Sender Consistency
        if (
            not investigation
            .sender_consistency_analysis
            .get(
                "consistent",
                True
            )
        ):
            score += rules.get(
                "sender_domain_mismatch",
                0
            )

        # Urgency Detection
        if (
            investigation.urgency_analysis
            .get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "urgency_detected",
                0
            )

        # Credential Request
        if (
            investigation
            .credential_request_analysis
            .get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "credential_request",
                0
            )

        # Financial Scam
        if (
            investigation
            .financial_scam_analysis
            .get(
                "detected",
                False
            )
        ):
            score += rules.get(
                "financial_scam",
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