from urllib.parse import urlparse


class ShortenedURLDetector:

    SHORTENERS = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "ow.ly",
        "is.gd",
        "cutt.ly",
        "rb.gy"
    ]

    def analyze(self, investigation):

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

                if (
                    hostname
                    and hostname.lower()
                    in self.SHORTENERS
                ):

                    result["detected"] = True

                    result["urls"].append(
                        url
                    )

            except Exception:
                pass

        investigation.url_analysis[
            "shortened_url"
        ] = result

        return investigation