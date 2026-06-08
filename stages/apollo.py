import requests
import os
from dotenv import load_dotenv

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def get_lookalike_companies(seed_domain, limit=5):
    try:
        headers = {
            "Content-Type": "application/json",
            "X-Api-Key": APOLLO_API_KEY
        }

        seed_resp = requests.post(
            "https://api.apollo.io/api/v1/organizations/enrich",
            headers=headers,
            json={"domain": seed_domain}
        )
        seed_resp.raise_for_status()
        seed_data = seed_resp.json().get("organization", {})
        industry = seed_data.get("industry", "technology")
        print(f"  Seed company industry: {industry}")

        search_resp = requests.post(
            "https://api.apollo.io/api/v1/mixed_companies/search",
            headers=headers,
            json={
                "keywords": industry,
                "page": 1,
                "per_page": limit + 1,
            }
        )
        search_resp.raise_for_status()
        orgs = search_resp.json().get("organizations", [])

        companies = []
        for org in orgs:
            domain = org.get("primary_domain", "")
            if domain and domain != seed_domain:
                companies.append({
                    "name": org.get("name", ""),
                    "domain": domain,
                    "industry": org.get("industry", ""),
                })
            if len(companies) >= limit:
                break

        return companies

    except requests.exceptions.RequestException as e:
        print(f"  ⚠️ Apollo API error: {e}")
        print("  Using fallback company list...")
        return get_fallback_companies(seed_domain)

def get_fallback_companies(seed_domain):
    fallbacks = {
        "stripe.com": [
            {"name": "Razorpay", "domain": "razorpay.com", "industry": "fintech"},
            {"name": "Square", "domain": "squareup.com", "industry": "fintech"},
            {"name": "Braintree", "domain": "braintreepayments.com", "industry": "fintech"},
        ],
        "shopify.com": [
            {"name": "BigCommerce", "domain": "bigcommerce.com", "industry": "ecommerce"},
            {"name": "WooCommerce", "domain": "woocommerce.com", "industry": "ecommerce"},
        ],
    }
    return fallbacks.get(seed_domain, [
        {"name": "Example Corp", "domain": "example-corp.com", "industry": "technology"},
    ])