import re
from urllib.parse import urlparse


class IPURLDetector:

    IPV4_REGEX = (
        r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    )

    def analyze(self, investigation):

        result = {
            "detected": False,
            "urls": []
        }

        for url in investigation.ioc_urls:

            try:

                parsed = urlparse(url)

                host = parsed.hostname

                if (
                    host
                    and re.match(
                        self.IPV4_REGEX,
                        host
                    )
                ):

                    result["detected"] = True

                    result["urls"].append(
                        url
                    )

            except Exception:
                pass

        investigation.url_analysis[
            "ip_url"
        ] = result

        return investigation