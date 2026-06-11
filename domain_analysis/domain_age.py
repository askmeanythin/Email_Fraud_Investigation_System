from datetime import datetime, timezone

import whois


class DomainAgeAnalyzer:

    def analyze(self, investigation):

        results = {}

        for domain in investigation.ioc_domains:

            try:

                domain_info = whois.whois(domain)

                creation_date = (
                    domain_info.creation_date
                )

                if isinstance(
                    creation_date,
                    list
                ):
                    creation_date = (
                        creation_date[0]
                    )

                if creation_date:

                    if (
                        creation_date.tzinfo
                        is None
                    ):
                        creation_date = (
                            creation_date.replace(
                                tzinfo=timezone.utc
                            )
                        )

                    current_time = (
                        datetime.now(
                            timezone.utc
                        )
                    )

                    age_days = (
                        current_time
                        - creation_date
                    ).days

                    results[domain] = {
                        "creation_date":
                            str(
                                creation_date.date()
                            ),
                        "age_days":
                            age_days
                    }

                else:

                    results[domain] = {
                        "creation_date": None,
                        "age_days": None
                    }

            except Exception as error:

                results[domain] = {
                    "error": str(error)
                }

        investigation.domain_age = results

        return investigation