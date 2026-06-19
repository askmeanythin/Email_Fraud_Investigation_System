from email_parser.parser import EmailParser

from header_analysis.reply_to_analyzer import (
    ReplyToAnalyzer
)

from header_analysis.return_path_analyzer import (
    ReturnPathAnalyzer
)

from header_analysis.sender_consistency_analyzer import (
    SenderConsistencyAnalyzer
)


def main():

    parser = EmailParser()

    reply_to = (
        ReplyToAnalyzer()
    )

    return_path = (
        ReturnPathAnalyzer()
    )

    consistency = (
        SenderConsistencyAnalyzer()
    )

    investigation = parser.parse_email(
        "data/sample_emails/sample.eml"
    )

    investigation = reply_to.analyze(
        investigation
    )

    investigation = return_path.analyze(
        investigation
    )

    investigation = consistency.analyze(
        investigation
    )

    print(
        "\n===== SENDER CONSISTENCY ====="
    )

    print(
        investigation
        .sender_consistency_analysis
    )


if __name__ == "__main__":
    main()