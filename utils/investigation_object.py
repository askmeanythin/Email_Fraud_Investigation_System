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

    # Investigation Results
    findings: Dict = field(default_factory=dict)

    # Final Analysis
    risk_score: int = 0
    classification: str = "Unknown"