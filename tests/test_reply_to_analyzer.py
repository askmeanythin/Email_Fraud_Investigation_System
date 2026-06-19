from email_parser.parser import EmailParser

from header_analysis.reply_to_analyzer import (
    ReplyToAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = (
        ReplyToAnalyzer()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== REPLY TO ANALYSIS ====="
    )

    print(
        investigation.reply_to_analysis
    )


if __name__ == "__main__":
    main()