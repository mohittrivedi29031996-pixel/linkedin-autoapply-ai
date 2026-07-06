from pathlib import Path
from playwright.sync_api import sync_playwright


class BrowserAgent:

    def launch(self):

        print("Launching Chrome...")

        profile_path = Path("browser_profile")

        with sync_playwright() as p:

            context = p.chromium.launch_persistent_context(
                user_data_dir=str(profile_path),
                headless=False
            )

            page = context.new_page()

            page.goto("https://www.linkedin.com/jobs")

            print("LinkedIn Jobs opened.")

            input("Press ENTER to close browser...")

            try:
                context.close()
            except Exception:
                pass