import re


class SenderConsistencyAnalyzer:

    EMAIL_REGEX = (
        r"[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    )

    def extract_domain(
        self,
        email_address
    ):

        if not email_address:
            return None

        match = re.search(
            self.EMAIL_REGEX,
            email_address
        )

        if not match:
            return None

        email = match.group()

        return (
            email.split("@")[1]
            .lower()
            .strip()
        )

    def analyze(self, investigation):

        result = {
            "consistent": True,
            "from_domain": None,
            "reply_to_domain": None,
            "return_path_domain": None,
            "mismatches": []
        }

        from_domain = (
            self.extract_domain(
                investigation.sender
            )
        )

        reply_to_domain = (
            self.extract_domain(
                investigation.reply_to_analysis.get(
                    "reply_to"
                )
            )
        )

        return_path_domain = (
            self.extract_domain(
                investigation.return_path_analysis.get(
                    "return_path"
                )
            )
        )

        result["from_domain"] = (
            from_domain
        )

        result["reply_to_domain"] = (
            reply_to_domain
        )

        result["return_path_domain"] = (
            return_path_domain
        )

        if (
            reply_to_domain
            and from_domain
            and reply_to_domain
            != from_domain
        ):

            result["consistent"] = (
                False
            )

            result["mismatches"].append(
                "Reply-To Domain Mismatch"
            )

        if (
            return_path_domain
            and from_domain
            and return_path_domain
            != from_domain
        ):

            result["consistent"] = (
                False
            )

            result["mismatches"].append(
                "Return-Path Domain Mismatch"
            )

        investigation.sender_consistency_analysis = (
            result
        )

        return investigation