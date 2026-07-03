# Startup Outreach Automation

Automated cold outreach pipeline — seed domain in, personalized emails out.

## How It Works

1. **Apollo.io** → finds lookalike companies from seed domain
2. **Prospeo** → extracts decision-maker contacts + verified emails
3. **Brevo** → sends personalized outreach emails from custom domain

## Features
- 🔍 Lookalike company discovery
- 👥 C-level contact extraction (CEO, CTO, Founder, VP)
- ✉️ Personalized emails via custom domain
- 📁 Auto-logs every email sent to `outreach_log.csv`
- ✅ Review contacts before sending
- 🛡️ Error handling, deduplication, rate limiting

## Setup

```bash
git clone https://github.com/ThejaswiniM02/startup-outreach-automation
cd startup-outreach-automation
pip install -r requirements.txt
```

Add keys to `.env`:
APOLLO_API_KEY=
PROSPEO_API_KEY=
BREVO_API_KEY=
SENDER_EMAIL=you@yourdomain.com
SENDER_NAME=Your Name

## Usage

```bash
python main.py smallcase.com
python main.py freshworks.com
```

**Built by Thejaswini M** · [GitHub](https://github.com/ThejaswiniM02) · [LinkedIn](https://linkedin.com/in/thejaswini-m)
