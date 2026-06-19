from email_parser.parser import EmailParser

from content_analysis.content_analyzer import (
    ContentAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = (
        ContentAnalyzer()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== CONTENT ANALYSIS ====="
    )

    print(
        "\nUrgency:"
    )

    print(
        investigation.urgency_analysis
    )

    print(
        "\nCredential Requests:"
    )

    print(
        investigation
        .credential_request_analysis
    )

    print(
        "\nFinancial Scam:"
    )

    print(
        investigation
        .financial_scam_analysis
    )


if __name__ == "__main__":
    main()