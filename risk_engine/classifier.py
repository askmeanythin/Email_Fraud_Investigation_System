class EmailClassifier:

    def classify(self, investigation):

        score = investigation.risk_score

        if score >= 60:

            investigation.classification = (
                "High Risk Phishing"
            )

        elif score >= 40:

            investigation.classification = (
                "Suspicious Email"
            )

        elif score >= 20:

            investigation.classification = (
                "Promotional Marketing Email"
            )

        else:

            investigation.classification = (
                "Legitimate Communication"
            )

        return investigation