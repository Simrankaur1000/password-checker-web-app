import hashlib

def sha1_hash(password):
    return hashlib.sha1(password.encode()).hexdigest().upper()

