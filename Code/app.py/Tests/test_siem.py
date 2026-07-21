from siem_engine import get_all_alerts

alerts = get_all_alerts()

print("Wazuh Alerts:", len(alerts["wazuh"]))
print("Splunk Alerts:", len(alerts["splunk"]))