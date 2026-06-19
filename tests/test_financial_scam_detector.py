from email_parser.parser import EmailParser

from content_analysis.financial_scam_detector import (
    FinancialScamDetector
)


def main():

    parser = EmailParser()

    detector = (
        FinancialScamDetector()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = detector.analyze(
        investigation
    )

    print(
        "\n===== FINANCIAL SCAM ANALYSIS ====="
    )

    print(
        investigation
        .financial_scam_analysis
    )


if __name__ == "__main__":
    main()