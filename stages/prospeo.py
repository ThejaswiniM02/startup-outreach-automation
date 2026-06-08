import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")

def get_decision_makers(companies):
    titles = ["CEO", "CTO", "CMO", "VP", "Director", "Founder", "Co-Founder", "Head"]
    all_contacts = []
    headers = {
        "Content-Type": "application/json",
        "X-KEY": PROSPEO_API_KEY
    }

    for company in companies[:3]:  # Limit to 3 companies to avoid rate limits
        domain = company.get("domain")
        company_name = company.get("name", domain)
        print(f"  🔍 Searching decision makers for {company_name} ({domain})...")

        try:
            payload = {
                "page": 1,
                "filters": {
                    "company": {
                        "websites": {"include": [domain]}
                    }
                }
            }

            resp = requests.post(
                "https://api.prospeo.io/search-person",
                headers=headers,
                json=payload
            )

            if resp.status_code == 429:
                print("    ⏳ Rate limit hit, waiting...")
                time.sleep(5)
                continue

            resp.raise_for_status()
            data = resp.json()
            results = data.get("results", [])

            for result in results[:8]:  # Limit per company
                person = result.get("person", {})
                if not person:
                    continue

                # Handle email being dict or string
                email_data = person.get("email")
                if isinstance(email_data, dict):
                    email = email_data.get("email") or list(email_data.values())[0] if email_data else None
                else:
                    email = email_data

                if not email or "@" not in email:
                    continue

                name = f"{person.get('first_name', '')} {person.get('last_name', '')}".strip() or "Decision Maker"
                title = person.get("title", "") or person.get("seniority", "")

                is_decision_maker = any(t.lower() in (title.lower()) for t in titles) or "founder" in title.lower()

                if is_decision_maker or not title:  # Include strong candidates
                    all_contacts.append({
                        "name": name,
                        "title": title,
                        "email": email,
                        "company": company_name,
                        "domain": domain,
                    })
                    print(f"    ✅ {name} | {title} | {email}")

            time.sleep(2)  # Increased delay to avoid rate limits

        except Exception as e:
            print(f"    ⚠️ Error for {domain}: {e}")
            continue

    # Deduplicate safely
    seen = set()
    unique = []
    for c in all_contacts:
        email = c.get("email")
        if email and email not in seen:
            seen.add(email)
            unique.append(c)

    print(f"\n✅ Total unique contacts: {len(unique)}")
    return unique