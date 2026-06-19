from email_parser.parser import EmailParser

from content_analysis.urgency_detector import (
    UrgencyDetector
)


def main():

    parser = EmailParser()

    detector = (
        UrgencyDetector()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = detector.analyze(
        investigation
    )

    print(
        "\n===== URGENCY ANALYSIS ====="
    )

    print(
        investigation.urgency_analysis
    )


if __name__ == "__main__":
    main()