from email_parser.parser import EmailParser

from url_analysis.suspicious_tld_detector import (
    SuspiciousTLDDetector
)


def main():

    parser = EmailParser()

    detector = (
        SuspiciousTLDDetector()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = detector.analyze(
        investigation
    )

    print(
        "\n===== SUSPICIOUS TLD ====="
    )

    print(
        investigation.url_analysis[
            "suspicious_tld"
        ]
    )


if __name__ == "__main__":
    main()