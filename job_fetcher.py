import requests

KEYWORDS = [
    "software engineer",
    "java developer",
    "backend developer",
    "full stack developer",
    "associate software engineer",
    "graduate engineer trainee"
]


def fetch_jobs():
    jobs = []

    # Sample Greenhouse boards
    greenhouse_boards = [
        "stripe",
        "discord",
        "notion",
        "airtable"
    ]

    for board in greenhouse_boards:

        try:
            url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

            response = requests.get(url, timeout=15)

            if response.status_code != 200:
                continue

            data = response.json()

            for job in data.get("jobs", []):

                title = job.get("title", "")

                if not any(
                    keyword.lower() in title.lower()
                    for keyword in KEYWORDS
                ):
                    continue

                jobs.append(
                    {
                        "company": board.title(),
                        "role": title,
                        "location": job.get("location", {}).get(
                            "name",
                            "Not Mentioned"
                        ),
                        "deadline": "Not Mentioned",
                        "requirements": "",
                        "apply_link": job.get(
                            "absolute_url",
                            ""
                        ),
                        "website": f"https://{board}.com",
                        "source": "greenhouse"
                    }
                )

        except Exception as e:
            print(f"Error: {board} -> {e}")

    return jobs
