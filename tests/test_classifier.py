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

from risk_engine.classifier import (
    EmailClassifier
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

    classifier = (
        EmailClassifier()
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

    investigation = classifier.classify(
        investigation
    )

    print("\n===== FINAL RESULT =====")

    print(
        f"Risk Score     : "
        f"{investigation.risk_score}"
    )

    print(
        f"Classification : "
        f"{investigation.classification}"
    )


if __name__ == "__main__":
    main()