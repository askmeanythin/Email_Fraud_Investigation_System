from email_parser.parser import EmailParser

from ioc_extraction.email_extractor import EmailExtractor
from ioc_extraction.domain_extractor import DomainExtractor
from ioc_extraction.ip_extractor import IPExtractor

from domain_analysis.brand_impersonation import (
    BrandImpersonationDetector
)
from domain_analysis.typosquatting import (
    TyposquattingDetector
)
from domain_analysis.domain_age import (
    DomainAgeAnalyzer
)

from url_analysis.ip_url_detector import (
    IPURLDetector
)
from url_analysis.shortened_url_detector import (
    ShortenedURLDetector
)
from url_analysis.suspicious_tld_detector import (
    SuspiciousTLDDetector
)

from header_analysis.authentication_analyzer import (
    AuthenticationAnalyzer
)
from header_analysis.reply_to_analyzer import (
    ReplyToAnalyzer
)
from header_analysis.return_path_analyzer import (
    ReturnPathAnalyzer
)
from header_analysis.sender_consistency_analyzer import (
    SenderConsistencyAnalyzer
)

from content_analysis.content_analyzer import (
    ContentAnalyzer
)

from risk_engine.risk_calculator import (
    RiskCalculator
)
from risk_engine.classifier import (
    EmailClassifier
)


def main():

    parser = EmailParser()

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    # IOC Extraction
    investigation = EmailExtractor().extract(
        investigation
    )

    investigation = DomainExtractor().extract(
        investigation
    )

    investigation = IPExtractor().extract(
        investigation
    )

    # Domain Analysis
    investigation = (
        BrandImpersonationDetector()
        .detect(investigation)
    )

    investigation = (
        TyposquattingDetector()
        .detect(investigation)
    )

    investigation = (
        DomainAgeAnalyzer()
        .analyze(investigation)
    )

    # URL Analysis
    investigation = (
        IPURLDetector()
        .analyze(investigation)
    )

    investigation = (
        ShortenedURLDetector()
        .analyze(investigation)
    )

    investigation = (
        SuspiciousTLDDetector()
        .analyze(investigation)
    )

    # Header Analysis
    investigation = (
        AuthenticationAnalyzer()
        .analyze(investigation)
    )

    investigation = (
        ReplyToAnalyzer()
        .analyze(investigation)
    )

    investigation = (
        ReturnPathAnalyzer()
        .analyze(investigation)
    )

    investigation = (
        SenderConsistencyAnalyzer()
        .analyze(investigation)
    )

    # Content Analysis
    investigation = (
        ContentAnalyzer()
        .analyze(investigation)
    )

    # Risk Engine
    investigation = (
        RiskCalculator()
        .calculate(investigation)
    )

    investigation = (
        EmailClassifier()
        .classify(investigation)
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

    print(
        "\n===== KEY FINDINGS ====="
    )

    print(
        "Typosquatting:",
        investigation.typosquatting
    )

    print(
        "Urgency:",
        investigation.urgency_analysis
    )

    print(
        "Credential Requests:",
        investigation.credential_request_analysis
    )

    print(
        "Financial Scam:",
        investigation.financial_scam_analysis
    )


if __name__ == "__main__":
    main()