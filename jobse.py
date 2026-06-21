import os
import json
import requests

from job_fetcher import fetch_jobs
from job_filters import score_job

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

with open("config.json", "r") as f:
    config = json.load(f)

jobs = fetch_jobs()

filtered_jobs = []

for job in jobs:

    score = score_job(job)

    if score >= config["min_match_score"]:
        job["match_score"] = score
        filtered_jobs.append(job)

filtered_jobs.sort(
    key=lambda x: x["match_score"],
    reverse=True
)

filtered_jobs = filtered_jobs[
    : config["max_jobs_per_run"]
]

if not filtered_jobs:

    message = """
🚀 JOBSE

No matching fresher jobs found.
"""

else:

    message = "🚀 JOBSE\n\n"

    for idx, job in enumerate(
        filtered_jobs,
        start=1
    ):

        message += f"""
Job #{idx}

Company:
{job['company']}

Role:
{job['role']}

Application Deadline:
{job['deadline']}

Location:
{job['location']}

Application Link:
{job['apply_link']}

Source:
{job['source']}

Company Website:
{job['website']}

Match Score:
{job['match_score']}%

--------------------------------

"""

url = (
    f"https://api.telegram.org/bot"
    f"{BOT_TOKEN}/sendMessage"
)

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)

print("Done")
