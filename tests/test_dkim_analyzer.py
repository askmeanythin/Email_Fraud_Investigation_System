from email_parser.parser import EmailParser

from header_analysis.dkim_analyzer import (
    DKIMAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = DKIMAnalyzer()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== DKIM ANALYSIS ====="
    )

    print(
        investigation.dkim_analysis
    )


if __name__ == "__main__":
    main()