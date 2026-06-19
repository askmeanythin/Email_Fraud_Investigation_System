from email_parser.parser import EmailParser

from header_analysis.authentication_analyzer import (
    AuthenticationAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = (
        AuthenticationAnalyzer()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== AUTHENTICATION ====="
    )

    print(
        "SPF   :",
        investigation.spf_analysis
    )

    print(
        "DKIM  :",
        investigation.dkim_analysis
    )

    print(
        "DMARC :",
        investigation.dmarc_analysis
    )


if __name__ == "__main__":
    main()