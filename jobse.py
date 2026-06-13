import json
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

with open("config.json", "r") as f:
    config = json.load(f)

message = f"""
🚀 JOBSE CONFIG TEST

Max Jobs Per Run: {config['max_jobs_per_run']}
Minimum Match Score: {config['min_match_score']}
Experience Limit: {config['experience_limit']}

Roles:
{chr(10).join(config['roles'][:5])}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Config Loaded Successfully")
