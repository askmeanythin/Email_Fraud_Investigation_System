class DMARCAnalyzer:

    def analyze(self, investigation):

        result = {
            "result": "unknown"
        }

        for (
            header,
            value
        ) in investigation.headers.items():

            if (
                header.lower()
                == "authentication-results"
            ):

                value = value.lower()

                if "dmarc=pass" in value:

                    result["result"] = (
                        "pass"
                    )

                elif "dmarc=fail" in value:

                    result["result"] = (
                        "fail"
                    )

        investigation.dmarc_analysis = (
            result
        )

        return investigation