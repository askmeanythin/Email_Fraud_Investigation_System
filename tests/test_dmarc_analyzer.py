from email_parser.parser import EmailParser

from header_analysis.dmarc_analyzer import (
    DMARCAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = DMARCAnalyzer()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== DMARC ANALYSIS ====="
    )

    print(
        investigation.dmarc_analysis
    )


if __name__ == "__main__":
    main()