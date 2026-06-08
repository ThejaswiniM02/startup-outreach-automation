# Cold Outreach Automation Pipeline

A Python-based automated cold outreach system built for Vocallabs / Subspace SDE Intern assignment.

This tool takes a seed company domain, finds similar companies, extracts decision-maker contacts, and sends personalized cold emails.

## Features

- 🔍 Finds lookalike companies using Apollo.io
- 👥 Extracts C-level / decision maker contacts using Prospeo
- ✉️ Sends personalized emails using Brevo (with custom domain)
- Modular, clean, and well-documented code
- Error handling + fallbacks

## Tech Stack

- Python 3
- Apollo.io API
- Prospeo API
- Brevo (Sendinblue) API
- python-dotenv

## Project Structure

```
vocallabs-pipeline/
├── main.py                 # Main entry point
├── stages/
│   ├── apollo.py           # Lookalike companies
│   ├── prospeo.py          # Decision makers & emails
│   └── brevo.py            # Email sending
├── .env                    # API keys (not committed)
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup & Installation

1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd vocallabs-pipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file (copy from `.env.example` if available) and add your keys:
   ```
   APOLLO_API_KEY=your_apollo_key
   PROSPEO_API_KEY=your_prospeo_key
   BREVO_API_KEY=your_brevo_key
   SENDER_EMAIL=outreach@yourdomain.website
   SENDER_NAME=Your Name
   ```

4. Verify your domain in Brevo (Settings → Senders & Domains)

## Usage

```bash
# Run with any company domain
python main.py razorpay.com

# Example
python main.py zoho.com
python main.py phonepe.com
```

## How It Works

1. **Apollo** → Finds 5 similar companies based on seed domain
2. **Prospeo** → Finds decision makers (CEO, CTO, VP etc.) + emails
3. **Brevo** → Sends personalized cold emails from your custom domain

## Demo

[Watch Demo Video]https://drive.google.com/file/d/19GHj_OraWvBQCy9BL7ni9E1hE469m5yx/view?usp=sharing

## Note

This project was built as part of Vocallabs/Subspace SDE Intern assignment (June 2026).


**Built by Thejaswini M**