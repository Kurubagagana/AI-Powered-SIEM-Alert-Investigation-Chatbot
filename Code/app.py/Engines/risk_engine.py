def calculate_risk(alert):

    score = 0

    severity = int(alert.get("severity", 0))

    # Severity Weight
    score += severity * 10

    # MITRE ATT&CK
    mitre = str(alert.get("mitre", "None"))

    if mitre != "None":
        score += 20

    # Critical Keywords
    event = alert.get("event", "").lower()

    critical_keywords = [
        "malware",
        "ransomware",
        "brute force",
        "privilege",
        "account changed",
        "failed login",
        "powershell",
        "remote",
        "attack",
        "credential",
        "administrator"
    ]

    for keyword in critical_keywords:

        if keyword in event:
            score += 10

    # Maximum score
    if score > 100:
        score = 100

    # Risk Level
    if score >= 90:
        level = "Critical"

    elif score >= 70:
        level = "High"

    elif score >= 40:
        level = "Medium"

    else:
        level = "Low"

    return {
        "score": score,
        "level": level
    }