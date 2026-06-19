from urllib.parse import urlparse

from utils.tld_loader import (
    TLDLoader
)


class SuspiciousTLDDetector:

    def analyze(self, investigation):

        tlds = (
            TLDLoader.load_tlds()
        )

        result = {
            "detected": False,
            "urls": []
        }

        for url in investigation.ioc_urls:

            try:

                hostname = (
                    urlparse(url)
                    .hostname
                )

                if not hostname:
                    continue

                hostname = (
                    hostname.lower()
                )

                for tld in tlds:

                    if hostname.endswith(
                        tld
                    ):

                        result[
                            "detected"
                        ] = True

                        result[
                            "urls"
                        ].append(url)

            except Exception:
                pass

        investigation.url_analysis[
            "suspicious_tld"
        ] = result

        return investigation