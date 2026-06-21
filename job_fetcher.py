import requests

KEYWORDS = [
    "intern",
    "associate",
    "graduate",
    "trainee",
    "new grad",
    "campus"
]

ALLOWED_LOCATIONS = [
    "india",
    "hyderabad",
    "bangalore",
    "pune",
    "chennai",
    "remote"
]


def location_allowed(location):
    location = location.lower()

    for city in ALLOWED_LOCATIONS:
        if city in location:
            return True

    return False


def fetch_jobs():
    jobs = []

    greenhouse_boards = [
        "stripe",
        "discord",
        "notion",
        "airtable"
    ]

    for board in greenhouse_boards:

        try:

            url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

            response = requests.get(
                url,
                timeout=15
            )

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

                location = job.get(
                    "location",
                    {}
                ).get(
                    "name",
                    "Not Mentioned"
                )

                if not location_allowed(location):
                    continue

                jobs.append(
                    {
                        "company": board.title(),
                        "role": title,
                        "location": location,
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
            print(
                f"Error fetching {board}: {e}"
            )

    return jobs
