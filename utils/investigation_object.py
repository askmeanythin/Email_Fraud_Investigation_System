from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class InvestigationObject:

    # Basic Email Information
    subject: str = ""
    sender: str = ""
    recipient: str = ""
    date: str = ""

    # Email Headers
    headers: Dict[str, str] = field(default_factory=dict)

    # Email Content
    plain_text_body: str = ""
    html_body: str = ""

    # Extracted Artifacts
    urls: List[str] = field(default_factory=list)
    attachments: List[str] = field(default_factory=list)

    # IOC Storage
    ioc_domains: List[str] = field(default_factory=list)
    ioc_ips: List[str] = field(default_factory=list)
    ioc_emails: List[str] = field(default_factory=list)
    ioc_urls: List[str] = field(default_factory=list)

    # Investigation Results
    findings: Dict = field(default_factory=dict)

    # Domain Analysis
    brand_impersonation: Dict = field(default_factory=dict)
    typosquatting: Dict = field(default_factory=dict)
    domain_age: Dict = field(default_factory=dict)

    # Email Authentication Analysis
    spf_analysis: Dict = field(default_factory=dict)
    dkim_analysis: Dict = field(default_factory=dict)
    dmarc_analysis: Dict = field(default_factory=dict)
    
    reply_to_analysis: Dict = field(default_factory=dict)
    return_path_analysis: Dict = field(default_factory=dict)
    sender_consistency_analysis: Dict = field(default_factory=dict)
    urgency_analysis: Dict = field(default_factory=dict)
    credential_request_analysis: Dict = field(default_factory=dict)
    financial_scam_analysis: Dict = field(default_factory=dict)

    # URL Analysis
    url_analysis: Dict = field(default_factory=dict)

    # Threat Intelligence
    threat_intelligence: Dict = field(default_factory=dict)

    # AI Analysis
    ai_summary: str = ""
    ai_recommendations: str = ""

    # Final Analysis
    risk_score: int = 0
    classification: str = "Unknown"