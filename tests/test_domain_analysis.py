from email_parser.parser import EmailParser
from ioc_extraction.email_extractor import EmailExtractor
from ioc_extraction.domain_extractor import DomainExtractor


def main():

    parser = EmailParser()
    email_extractor = EmailExtractor()
    domain_extractor = DomainExtractor()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = email_extractor.extract(
        investigation
    )

    investigation = domain_extractor.extract(
        investigation
    )

    print("\n===== DOMAIN IOCs =====")

    for domain in investigation.ioc_domains:
        print(domain)


if __name__ == "__main__":
    main()