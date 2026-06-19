from email_parser.parser import EmailParser

from content_analysis.credential_request_detector import (
    CredentialRequestDetector
)


def main():

    parser = EmailParser()

    detector = (
        CredentialRequestDetector()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = detector.analyze(
        investigation
    )

    print(
        "\n===== CREDENTIAL REQUEST ANALYSIS ====="
    )

    print(
        investigation
        .credential_request_analysis
    )


if __name__ == "__main__":
    main()