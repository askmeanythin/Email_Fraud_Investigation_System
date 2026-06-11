from email_parser.parser import EmailParser

from ioc_extraction.email_extractor import EmailExtractor
from ioc_extraction.domain_extractor import DomainExtractor

from domain_analysis.brand_impersonation import (
    BrandImpersonationDetector
)


def main():

    parser = EmailParser()

    email_extractor = EmailExtractor()
    domain_extractor = DomainExtractor()

    detector = BrandImpersonationDetector()

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

    print("\n===== BRAND IMPERSONATION =====")

    print(
        f"Detected   : "
        f"{investigation.brand_impersonation['detected']}"
    )

    print(
        f"Brand      : "
        f"{investigation.brand_impersonation['brand']}"
    )

    print(
        f"Domain     : "
        f"{investigation.brand_impersonation['domain']}"
    )

    print(
        f"Confidence : "
        f"{investigation.brand_impersonation['confidence']}"
    )


if __name__ == "__main__":
    main()