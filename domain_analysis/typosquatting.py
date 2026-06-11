from utils.brand_loader import BrandLoader
from utils.typosquatting_loader import TyposquattingLoader


class TyposquattingDetector:

    def normalize_domain(
        self,
        domain,
        replacements,
        suspicious_words
    ):

        root = domain.split(".")[0].lower()

        for word in suspicious_words:
            root = root.replace(word, "")

        root = root.replace("-", "")

        for old, new in replacements.items():
            root = root.replace(old, new)

        return root

    def detect(self, investigation):

        brands = BrandLoader.load_brands()

        replacements = (
            TyposquattingLoader.load_replacements()
        )

        suspicious_words = (
            TyposquattingLoader.load_suspicious_words()
        )

        result = {
            "detected": False,
            "brand": None,
            "domain": None
        }

        for domain in investigation.ioc_domains:

            normalized = self.normalize_domain(
                domain,
                replacements,
                suspicious_words
            )

            for brand in brands.keys():

                if normalized == brand:

                    result = {
                        "detected": True,
                        "brand": brand,
                        "domain": domain
                    }

        investigation.typosquatting = result

        return investigation