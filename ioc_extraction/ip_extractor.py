import re


class IPExtractor:

    IPV4_REGEX = (
        r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    )

    def extract(self, investigation):

        ips = set()

        text_sources = [
            investigation.plain_text_body,
            investigation.html_body
        ]

        for value in investigation.headers.values():
            text_sources.append(str(value))

        for text in text_sources:

            found_ips = re.findall(
                self.IPV4_REGEX,
                text
            )

            ips.update(found_ips)

        investigation.ioc_ips = sorted(
            list(ips)
        )

        return investigation