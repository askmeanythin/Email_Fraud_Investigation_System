import re
from urllib.parse import urlparse


class DomainExtractor:

    def extract(self, investigation):

        domains = set()

        # Domains from email IOCs
        for email in investigation.ioc_emails:

            try:
                domain = email.split("@")[1].lower()
                domains.add(domain)

            except Exception:
                pass

        # Domains from URLs
        for url in investigation.urls:

            try:
                parsed = urlparse(url)

                if parsed.netloc:
                    domains.add(
                        parsed.netloc.lower()
                    )

            except Exception:
                pass

        investigation.ioc_domains = sorted(
            list(domains)
        )

        return investigation