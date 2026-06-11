from email_parser.parser import EmailParser

from ioc_extraction.email_extractor import (
    EmailExtractor
)

from ioc_extraction.domain_extractor import (
    DomainExtractor
)

from domain_analysis.domain_age import (
    DomainAgeAnalyzer
)


def main():

    parser = EmailParser()

    email_extractor = EmailExtractor()

    domain_extractor = DomainExtractor()

    analyzer = DomainAgeAnalyzer()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = email_extractor.extract(
        investigation
    )

    investigation = domain_extractor.extract(
        investigation
    )

    investigation = analyzer.analyze(
        investigation
    )

    print(
        "\n===== DOMAIN AGE ====="
    )

    for (
        domain,
        data
    ) in investigation.domain_age.items():

        print(
            f"\nDomain: {domain}"
        )

        for (
            key,
            value
        ) in data.items():

            print(
                f"{key}: {value}"
            )


if __name__ == "__main__":
    main()