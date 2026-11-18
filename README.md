# Password Strength Checker & Breach Alert

A Flask-based web application that evaluates password strength, checks whether a password appears in known breach data through the Have I Been Pwned (HIBP) API, and suggests stronger alternatives.

## Features

- Password strength classification using length, character diversity, and entropy-related checks.
- Breach exposure lookup using the HIBP range API and SHA-1 k-anonymity model.
- Strong password suggestions.
- Lightweight browser-based interface.

## Technology

- Python
- Flask
- HTML templates
- Have I Been Pwned API

## Run locally

```bash
git clone https://github.com/Simrankaur1000/password-checker-web-app.git
cd password-checker-web-app
pip install -r requirements.txt
python app.py
```

Open the local URL printed by Flask in your browser.

## Security and privacy notes

- The HIBP range approach sends only a short prefix of the SHA-1 hash to the service; the full password is not sent to HIBP.
- Never test with a password you currently use on a real account.
- Do not deploy this demonstration with real user credentials without a security review, HTTPS, secure session handling, rate limiting, and appropriate secret management.
- A breach lookup is an exposure signal, not proof that an account is currently compromised.

## Project scope

This is an educational security project. Its strength classification is a guide and should not be treated as a complete password-auditing standard.

## Author

Simran Kaur · [Portfolio](https://portfolio-k3wf.vercel.app)
