from email import policy
from email.parser import BytesParser
import re




from utils.investigation_object import InvestigationObject


class EmailParser:

    URL_REGEX = r"https?://[^\s<>\"']+"

    def parse_email(self, file_path: str) -> InvestigationObject:

        with open(file_path, "rb") as file:
            msg = BytesParser(policy=policy.default).parse(file)

        investigation = InvestigationObject()

        # Basic Information
        investigation.subject = str(msg.get("Subject", ""))
        investigation.sender = str(msg.get("From", ""))
        investigation.recipient = str(msg.get("To", ""))
        investigation.date = str(msg.get("Date", ""))

        # Headers
        for key, value in msg.items():
            investigation.headers[key] = str(value)

        # Body Extraction
        plain_text_parts = []
        html_parts = []

        if msg.is_multipart():

            for part in msg.walk():

                content_type = part.get_content_type()

                filename = part.get_filename()

                if filename:
                    investigation.attachments.append(filename)

                try:
                    payload = part.get_content()

                    if content_type == "text/plain":
                        plain_text_parts.append(str(payload))

                    elif content_type == "text/html":
                        html_parts.append(str(payload))

                except Exception:
                    continue

        else:

            try:
                payload = msg.get_content()

                if msg.get_content_type() == "text/plain":
                    plain_text_parts.append(str(payload))

                elif msg.get_content_type() == "text/html":
                    html_parts.append(str(payload))

            except Exception:
                pass

        investigation.plain_text_body = "\n".join(plain_text_parts)
        investigation.html_body = "\n".join(html_parts)

        combined_text = (
            investigation.plain_text_body
            + "\n"
            + investigation.html_body
        )

        urls = re.findall(
            self.URL_REGEX,
            combined_text
        )

        investigation.urls = list(set(urls))
        investigation.ioc_urls = investigation.urls.copy()

        return investigation