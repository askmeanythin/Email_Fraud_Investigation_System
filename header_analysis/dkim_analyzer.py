class DKIMAnalyzer:

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

                if "dkim=pass" in value:

                    result["result"] = (
                        "pass"
                    )

                elif "dkim=fail" in value:

                    result["result"] = (
                        "fail"
                    )

        investigation.dkim_analysis = (
            result
        )

        return investigation