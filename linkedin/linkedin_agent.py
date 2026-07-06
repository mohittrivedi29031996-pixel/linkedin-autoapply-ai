from urllib.parse import quote

from config.settings import TARGET_LOCATIONS
from config.settings import TARGET_ROLES


class LinkedInAgent:

    def search_jobs(self, page):

        total_searches = len(TARGET_ROLES) * len(TARGET_LOCATIONS)

        print(f"\nStarting {total_searches} searches...\n")

        count = 1

        for role in TARGET_ROLES:

            for location in TARGET_LOCATIONS:

                print(f"[{count}/{total_searches}] {role} -> {location}")

                url = (
                    "https://www.linkedin.com/jobs/search/"
                    f"?keywords={quote(role)}"
                    f"&location={quote(location)}"
                )

                page.goto(url)

                page.wait_for_timeout(4000)

                count += 1

        print("\nAll searches completed.")