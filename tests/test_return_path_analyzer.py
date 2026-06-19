from email_parser.parser import EmailParser

from header_analysis.return_path_analyzer import (
    ReturnPathAnalyzer
)


def main():

    parser = EmailParser()

    analyzer = (
        ReturnPathAnalyzer()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== RETURN PATH ANALYSIS ====="
    )

    print(
        investigation.return_path_analysis
    )


if __name__ == "__main__":
    main()