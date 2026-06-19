class ReturnPathAnalyzer:

    def analyze(self, investigation):

        result = {
            "detected": False,
            "return_path": None
        }

        for (
            header,
            value
        ) in investigation.headers.items():

            if (
                header.lower()
                == "return-path"
            ):

                result = {
                    "detected": True,
                    "return_path": value
                }

        investigation.return_path_analysis = (
            result
        )

        return investigation