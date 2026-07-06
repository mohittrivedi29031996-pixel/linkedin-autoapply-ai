from browser.browser_agent import BrowserAgent
from agents.job_finder import JobFinder


def main():

    print("=" * 50)
    print("LinkedIn AutoApply AI")
    print("=" * 50)

    browser = BrowserAgent()
    browser.launch()

    finder = JobFinder()
    finder.search()


if __name__ == "__main__":
    main()