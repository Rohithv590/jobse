import os
import json
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

with open("config.json", "r") as f:
    config = json.load(f)

with open("test_jobs.json", "r") as f:
    jobs = json.load(f)

message = "🚀 JOBSE\n\n"

for idx, job in enumerate(jobs[:config["max_jobs_per_run"]], start=1):
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

Company Website:
{job['website']}

Match Score:
85%

Reason:
Matches target role and skills.

--------------------------------
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)

print("Jobs sent successfully")
