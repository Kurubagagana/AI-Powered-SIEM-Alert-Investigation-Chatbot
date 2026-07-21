import requests

API_KEY = "YOUR_ABUSEIPDB_API_KEY"

URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip(ip):

    if ip in ("Unknown", "", None):
        return {
            "country": "-",
            "score": 0,
            "reputation": "Unknown"
        }

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:

        response = requests.get(
            URL,
            headers=headers,
            params=params,
            timeout=10
        )

        data = response.json()["data"]

        score = data["abuseConfidenceScore"]

        if score >= 80:
            reputation = "Malicious"
        elif score >= 40:
            reputation = "Suspicious"
        else:
            reputation = "Trusted"

        return {
            "country": data["countryCode"],
            "score": score,
            "reputation": reputation
        }

    except Exception:

        return {
            "country": "-",
            "score": 0,
            "reputation": "Unknown"
        }