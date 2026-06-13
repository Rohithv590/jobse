import os
import json
import requests
from job_fetcher import fetch_jobs

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

# Load sent jobs
with open("sent_jobs.json", "r") as f:
    sent_jobs = json.load(f)

jobs = fetch_jobs()

new_jobs = []

for job in jobs:
    job_id = f"{job['company']}_{job['role']}"

    if job_id not in sent_jobs:
        new_jobs.append(job)
        sent_jobs.append(job_id)

if not new_jobs:
    message = "🚀 JOBSE\n\nNo new jobs found."
else:
    message = "🚀 JOBSE\n\n"

    for idx, job in enumerate(
        new_jobs[:config["max_jobs_per_run"]],
        start=1
    ):
        message += f"""
Job #{idx}

Company:
{job['company']}

Role:
{job['role']}

Requirements:
{job['requirements']}

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

--------------------------------
"""

# Save updated sent jobs
with open("sent_jobs.json", "w") as f:
    json.dump(sent_jobs, f, indent=2)

# Send Telegram
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)

print("Done")
