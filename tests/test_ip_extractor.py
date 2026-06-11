from email_parser.parser import EmailParser
from ioc_extraction.ip_extractor import IPExtractor


def main():

    parser = EmailParser()
    extractor = IPExtractor()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = extractor.extract(
        investigation
    )

    print("\n===== IP IOCs =====")

    for ip in investigation.ioc_ips:
        print(ip)


if __name__ == "__main__":
    main()