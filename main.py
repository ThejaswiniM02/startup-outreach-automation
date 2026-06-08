import sys
from stages.apollo import get_lookalike_companies
from stages.prospeo import get_decision_makers
from stages.brevo import send_emails

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <seed_domain>")
        print("Example: python main.py stripe.com")
        sys.exit(1)

    seed_domain = sys.argv[1]
    print(f"\n🚀 Starting cold outreach pipeline for: {seed_domain}\n")

    print("📡 Stage 1: Finding lookalike companies via Apollo...")
    companies = get_lookalike_companies(seed_domain)
    if not companies:
        print("❌ No lookalike companies found. Exiting.")
        sys.exit(1)
    print(f"✅ Found {len(companies)} lookalike companies\n")

    print("🔍 Stage 2: Finding decision makers via Prospeo...")
    contacts = get_decision_makers(companies)
    if not contacts:
        print("❌ No contacts found. Exiting.")
        sys.exit(1)
    print(f"✅ Found {len(contacts)} contacts\n")

    print("=" * 50)
    print("📋 SUMMARY — Review before sending emails:")
    print("=" * 50)
    for c in contacts:
        print(f"  • {c.get('name')} | {c.get('title')} | {c.get('email')} | {c.get('company')}")
    print("=" * 50)

    confirm = input(f"\n⚠️  About to send {len(contacts)} emails. Proceed? (yes/no): ")
    if confirm.lower() != "yes":
        print("Aborted. No emails sent.")
        sys.exit(0)

    print("\n📧 Stage 3: Sending emails via Brevo...")
    send_emails(contacts)
    print("\n✅ Pipeline complete!")

if __name__ == "__main__":
    main()