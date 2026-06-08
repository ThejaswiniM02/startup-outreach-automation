import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_NAME = os.getenv("SENDER_NAME", "Thejaswini M")

def build_email(contact):
    name = contact.get("name", "there")
    company = contact.get("company", "your company")
    title = contact.get("title", "")

    subject = f"Quick question about {company}'s growth"
    body = f"""Hi {name},

I came across {company} and was impressed by what you're building.

I'm reaching out because I've been working on automation tools that help companies like yours streamline outreach and lead generation — reducing manual work while increasing conversion rates.

Given your role{f' as {title}' if title else ''} at {company}, I thought this might be relevant to challenges you're facing around scaling outreach efficiently.

Would you be open to a quick 15-minute call this week to explore if there's a fit?

Best regards,
Thejaswini M
tmdev.website
"""
    return subject, body

def send_emails(contacts):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "api-key": BREVO_API_KEY
    }

    sent = 0
    failed = 0

    for contact in contacts:
        email = contact.get("email")
        if not email:
            continue

        subject, body = build_email(contact)

        payload = {
            "sender": {"name": SENDER_NAME, "email": SENDER_EMAIL},
            "to": [{"email": email, "name": contact.get("name", "")}],
            "subject": subject,
            "textContent": body
        }

        try:
            resp = requests.post(
                "https://api.brevo.com/v3/smtp/email",
                headers=headers,
                json=payload
            )
            resp.raise_for_status()
            print(f"  ✅ Sent to {contact.get('name')} ({email})")
            sent += 1
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"  ❌ Failed to send to {email}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"     {e.response.text}")
            failed += 1

    print(f"\n📊 Results: {sent} sent, {failed} failed")