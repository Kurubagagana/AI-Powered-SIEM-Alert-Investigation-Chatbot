import json

ALERT_FILE = "/var/ossec/logs/alerts/alerts.json"

def get_wazuh_alerts(limit=10):
    try:
        alerts = []

        with open(ALERT_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    alerts.append(json.loads(line))

        return alerts[-limit:]

    except Exception as e:
        print("Error reading Wazuh alerts:", e)
        return []