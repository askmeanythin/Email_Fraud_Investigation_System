from email_parser.parser import EmailParser

from ioc_extraction.email_extractor import (
    EmailExtractor
)

from ioc_extraction.domain_extractor import (
    DomainExtractor
)

from domain_analysis.brand_impersonation import (
    BrandImpersonationDetector
)

from domain_analysis.typosquatting import (
    TyposquattingDetector
)

from domain_analysis.domain_age import (
    DomainAgeAnalyzer
)

from risk_engine.risk_calculator import (
    RiskCalculator
)


def main():

    parser = EmailParser()

    email_extractor = EmailExtractor()

    domain_extractor = DomainExtractor()

    brand_detector = (
        BrandImpersonationDetector()
    )

    typo_detector = (
        TyposquattingDetector()
    )

    age_analyzer = (
        DomainAgeAnalyzer()
    )

    risk_calculator = (
        RiskCalculator()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = email_extractor.extract(
        investigation
    )

    investigation = domain_extractor.extract(
        investigation
    )

    investigation = brand_detector.detect(
        investigation
    )

    investigation = typo_detector.detect(
        investigation
    )

    investigation = age_analyzer.analyze(
        investigation
    )

    investigation = risk_calculator.calculate(
        investigation
    )

    print(
        "\n===== RISK SCORE ====="
    )

    print(
        f"Score : "
        f"{investigation.risk_score}"
    )


if __name__ == "__main__":
    main()