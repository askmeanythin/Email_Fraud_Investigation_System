from header_analysis.spf_analyzer import (
    SPFAnalyzer
)

from header_analysis.dkim_analyzer import (
    DKIMAnalyzer
)

from header_analysis.dmarc_analyzer import (
    DMARCAnalyzer
)


class AuthenticationAnalyzer:

    def analyze(self, investigation):

        spf = SPFAnalyzer()
        dkim = DKIMAnalyzer()
        dmarc = DMARCAnalyzer()

        investigation = spf.analyze(
            investigation
        )

        investigation = dkim.analyze(
            investigation
        )

        investigation = dmarc.analyze(
            investigation
        )

        return investigation