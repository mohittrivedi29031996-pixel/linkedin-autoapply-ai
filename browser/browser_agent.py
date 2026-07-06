from pathlib import Path

from playwright.sync_api import sync_playwright

from linkedin.linkedin_agent import LinkedInAgent


class BrowserAgent:

    def launch(self):

        profile = Path("browser_profile")

        with sync_playwright() as p:

            context = p.chromium.launch_persistent_context(

                user_data_dir=str(profile),
                headless=False

            )

            page = context.new_page()

            linkedin = LinkedInAgent()

            linkedin.search_jobs(page)

            input("\nPress ENTER to close browser...")

            context.close()