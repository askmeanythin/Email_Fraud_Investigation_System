from content_analysis.urgency_detector import (
    UrgencyDetector
)

from content_analysis.credential_request_detector import (
    CredentialRequestDetector
)

from content_analysis.financial_scam_detector import (
    FinancialScamDetector
)


class ContentAnalyzer:

    def analyze(self, investigation):

        urgency = (
            UrgencyDetector()
        )

        credential = (
            CredentialRequestDetector()
        )

        financial = (
            FinancialScamDetector()
        )

        investigation = urgency.analyze(
            investigation
        )

        investigation = credential.analyze(
            investigation
        )

        investigation = financial.analyze(
            investigation
        )

        return investigation