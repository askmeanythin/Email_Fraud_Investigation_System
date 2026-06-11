from difflib import SequenceMatcher

from utils.brand_loader import BrandLoader


class BrandImpersonationDetector:

    def detect(self, investigation):

        brands = BrandLoader.load_brands()

        result = {
            "detected": False,
            "brand": None,
            "domain": None,
            "confidence": 0
        }

        for domain in investigation.ioc_domains:

            domain_lower = domain.lower()

            for brand_name in brands:

                similarity = SequenceMatcher(
                    None,
                    brand_name,
                    domain_lower
                ).ratio()

                if similarity >= 0.70:

                    result = {
                        "detected": True,
                        "brand": brand_name,
                        "domain": domain,
                        "confidence": round(
                            similarity * 100,
                            2
                        )
                    }

        investigation.brand_impersonation = result

        return investigation