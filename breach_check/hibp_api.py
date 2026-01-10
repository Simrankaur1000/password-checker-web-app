import requests

def check_breach(sha1_hash):
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return 0

    hashes = (line.split(":") for line in response.text.splitlines())

    for h, count in hashes:
        if h == suffix:
            return int(count)

    return 0

