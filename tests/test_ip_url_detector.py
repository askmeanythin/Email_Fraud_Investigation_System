from email_parser.parser import EmailParser

from url_analysis.ip_url_detector import (
    IPURLDetector
)


def main():

    parser = EmailParser()

    detector = IPURLDetector()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = detector.analyze(
        investigation
    )

    print(
        "\n===== IP URL DETECTION ====="
    )

    print(
        investigation.url_analysis[
            "ip_url"
        ]
    )


if __name__ == "__main__":
    main()