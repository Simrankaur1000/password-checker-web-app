from strength_checker.scorer import score_password, suggest_password
from breach_check.hash_utils import sha1_hash
from breach_check.hibp_api import check_breach

password = input("Enter password to check: ")

strength = score_password(password)
hashed = sha1_hash(password)
breach_count = check_breach(hashed)

print("\nPassword Strength:", strength)

if breach_count > 0:
    print(f"⚠️ Found in {breach_count} known data breaches!")
else:
    print("✅ No breach found.")

# Suggest a strong password if weak
if strength in ["Very Weak", "Weak", "Moderate"]:
    print("💡 Suggested Strong Password:", suggest_password())


