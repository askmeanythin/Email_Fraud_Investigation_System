import re

EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


class EmailExtractor:

    def extract(self, investigation):

        emails = set()

        # Basic fields
        emails.update(
            re.findall(
                EMAIL_REGEX,
                investigation.sender
            )
        )

        emails.update(
            re.findall(
                EMAIL_REGEX,
                investigation.recipient
            )
        )

        # Email body
        body_text = (
            investigation.plain_text_body
            + "\n"
            + investigation.html_body
        )

        emails.update(
            re.findall(
                EMAIL_REGEX,
                body_text
            )
        )

        # Headers
        for value in investigation.headers.values():

            emails.update(
                re.findall(
                    EMAIL_REGEX,
                    str(value)
                )
            )

        investigation.ioc_emails = sorted(
            list(emails)
        )

        return investigation