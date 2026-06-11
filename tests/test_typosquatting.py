from email_parser.parser import EmailParser

from ioc_extraction.email_extractor import EmailExtractor
from ioc_extraction.domain_extractor import DomainExtractor

from domain_analysis.typosquatting import (
    TyposquattingDetector
)


def main():

    parser = EmailParser()

    email_extractor = EmailExtractor()
    domain_extractor = DomainExtractor()

    detector = TyposquattingDetector()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = email_extractor.extract(
        investigation
    )

    investigation = domain_extractor.extract(
        investigation
    )

    investigation = detector.detect(
        investigation
    )

    print("\n===== TYPOSQUATTING =====")

    print(
        f"Detected : "
        f"{investigation.typosquatting['detected']}"
    )

    print(
        f"Brand    : "
        f"{investigation.typosquatting['brand']}"
    )

    print(
        f"Domain   : "
        f"{investigation.typosquatting['domain']}"
    )


if __name__ == "__main__":
    main()