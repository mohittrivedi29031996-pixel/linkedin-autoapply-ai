import json
from pathlib import Path
from urllib.parse import quote

from config.settings import (
    TARGET_LOCATIONS,
    TARGET_ROLES,
    MAX_JOBS_PER_SEARCH,
)


class LinkedInAgent:

    def search_jobs(self, page):

        total_searches = len(TARGET_ROLES) * len(TARGET_LOCATIONS)

        print(f"\nStarting {total_searches} searches...\n")

        count = 1

        storage = Path("storage")
        storage.mkdir(exist_ok=True)

        jobs_file = storage / "jobs.json"

        if jobs_file.exists():
            try:
                with open(jobs_file, "r", encoding="utf-8") as f:
                    all_jobs = json.load(f)
            except Exception:
                all_jobs = []
        else:
            all_jobs = []

        for role in TARGET_ROLES:

            for location in TARGET_LOCATIONS:

                print("=" * 60)
                print(f"[{count}/{total_searches}] {role} -> {location}")

                url = (
                    "https://www.linkedin.com/jobs/search/"
                    f"?keywords={quote(role)}"
                    f"&location={quote(location)}"
                )

                page.goto(url)

                page.wait_for_timeout(5000)

                cards = page.locator("div[data-job-id]")

                total_cards = min(cards.count(), MAX_JOBS_PER_SEARCH)

                print(f"Found {total_cards} jobs")

                for i in range(total_cards):

                    card = cards.nth(i)

                    try:

                        job_id = card.get_attribute("data-job-id") or ""

                        title = (
                            card.locator(
                                "a.job-card-list__title--link"
                            )
                            .inner_text()
                            .split("\n")[0]
                            .strip()
                        )

                        company = (
                            card.locator(
                                ".artdeco-entity-lockup__subtitle"
                            )
                            .inner_text()
                            .strip()
                        )

                        location_name = (
                            card.locator(
                                ".job-card-container__metadata-wrapper li"
                            )
                            .inner_text()
                            .strip()
                        )

                        href = card.locator(
                            "a.job-card-list__title--link"
                        ).get_attribute("href")

                        if href:
                            job_url = "https://www.linkedin.com" + href
                        else:
                            job_url = ""

                        duplicate = False

                        for job in all_jobs:
                            if job.get("job_id") == job_id:
                                duplicate = True
                                break

                        if duplicate:
                            continue

                        all_jobs.append(
                            {
                                "job_id": job_id,
                                "title": title,
                                "company": company,
                                "location": location_name,
                                "url": job_url,
                                "search_role": role,
                                "search_location": location,
                            }
                        )

                    except Exception:
                        continue

                print(
                    f"Collected {total_cards} jobs | Total saved: {len(all_jobs)}"
                )

                count += 1

        with open(jobs_file, "w", encoding="utf-8") as f:
            json.dump(
                all_jobs,
                f,
                indent=4,
                ensure_ascii=False,
            )

        print("\nFinished all searches.")