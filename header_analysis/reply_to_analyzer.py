class ReplyToAnalyzer:

    def analyze(self, investigation):

        result = {
            "detected": False,
            "reply_to": None
        }

        for (
            header,
            value
        ) in investigation.headers.items():

            if (
                header.lower()
                == "reply-to"
            ):

                result = {
                    "detected": True,
                    "reply_to": value
                }

        investigation.reply_to_analysis = (
            result
        )

        return investigation