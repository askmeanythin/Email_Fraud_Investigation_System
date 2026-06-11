from email_parser.parser import EmailParser
from ioc_extraction.email_extractor import EmailExtractor


def main():

    parser = EmailParser()
    extractor = EmailExtractor()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = extractor.extract(
        investigation
    )

    print("\n===== EMAIL IOCs =====")

    for email in investigation.ioc_emails:
        print(email)


if __name__ == "__main__":
    main()
    