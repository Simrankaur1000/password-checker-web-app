
# Password Strength Checker & Breach Alert Web Application

## Overview
This is a **web-based application** that allows users to:
- Check the **strength of a password** using entropy-based analysis.
- Verify if a password has been **compromised in known data breaches** using the HIBP (Have I Been Pwned) API.
- Receive **suggested strong passwords** if the input password is weak.

The application is built using **Python** and **Flask**, with a simple web interface.

---

## Features
- **Password Strength Analysis**
  - Very Weak, Weak, Moderate, Strong, Very Strong
  - Based on length, character diversity, and entropy
- **Breach Detection**
  - Checks password against HIBP database
  - Privacy-preserving via SHA-1 k-anonymity
- **Password Suggestions**
  - Randomly generates strong passwords with letters, numbers, and symbols
- **Web Interface**
  - Simple and user-friendly Flask-based frontend

---

## Technology Stack
- **Backend:** Python, Flask
- **Frontend:** HTML templates 
- **API:** HIBP API for breach detection
- **Security:** SHA-1 hashing, privacy-preserving checks
- **Version Control:** Git/GitHub

---

