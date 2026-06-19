from email_parser.parser import EmailParser

from header_analysis.spf_analyzer import (
    SPFAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = SPFAnalyzer()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== SPF ANALYSIS ====="
    )

    print(
        investigation.spf_analysis
    )


if __name__ == "__main__":
    main()