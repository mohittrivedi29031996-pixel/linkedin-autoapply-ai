class JobFinder:

    def search(self):

        print("=" * 50)
        print("Job Finder Agent")
        print("=" * 50)

        keywords = [
            "CSR Manager",
            "Programme Manager",
            "Program Manager",
            "CSR",
            "ESG",
            "Social Impact",
            "Community Engagement"
        ]

        print("Target Roles:")

        for job in keywords:
            print(f"• {job}")

        print("\nReady to search LinkedIn jobs.")