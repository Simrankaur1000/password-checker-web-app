from .entropy import calculate_entropy
import random
import string

def score_password(password):
    entropy = calculate_entropy(password)

    if len(password) < 8:
        return "Very Weak"
    elif entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"

def suggest_password(length=12):
    """Generate a strong random password"""
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(all_chars) for _ in range(length))
