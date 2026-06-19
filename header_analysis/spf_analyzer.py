class SPFAnalyzer:

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
                == "received-spf"
            ):

                value = value.lower()

                if "pass" in value:

                    result["result"] = (
                        "pass"
                    )

                elif "fail" in value:

                    result["result"] = (
                        "fail"
                    )

                else:

                    result["result"] = (
                        "unknown"
                    )

        investigation.spf_analysis = (
            result
        )

        return investigation