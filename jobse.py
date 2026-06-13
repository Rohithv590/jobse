import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """
JOBSE

System Started Successfully

Monitoring:
✓ Java Internships
✓ Software Engineer Internships
✓ Full Stack Roles

Next update in 6 hours.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print("Message Sent")
