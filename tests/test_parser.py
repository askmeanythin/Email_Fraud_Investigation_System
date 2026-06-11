from email_parser.parser import EmailParser


def main():

    parser = EmailParser()

    result = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    print("\n===== EMAIL DETAILS =====")

    print(f"Subject   : {result.subject}")
    print(f"From      : {result.sender}")
    print(f"To        : {result.recipient}")
    print(f"Date      : {result.date}")

    print("\n===== HEADERS =====")
    print(f"Total Headers: {len(result.headers)}")

    print("\n===== PLAIN TEXT BODY =====")
    print(result.plain_text_body)

    print("\n===== HTML BODY =====")
    print(result.html_body)

    print("\n===== URLS =====")

    for url in result.urls:
        print(url)

    print("\n===== ATTACHMENTS =====")

    for attachment in result.attachments:
        print(attachment)

if __name__ == "__main__":
    main()