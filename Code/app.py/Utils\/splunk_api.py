import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SPLUNK_URL = "https://172.29.84.216:8089"
USERNAME = "admin"
PASSWORD = "Gagana@123"   # Replace with your current password


def get_splunk_alerts():

    url = f"{SPLUNK_URL}/services/search/jobs/export"

    search_query = """
    search index=main
    | table _time host source _raw
    | head 20
    """

    payload = {
        "search": search_query,
        "output_mode": "json"
    }

    try:

        response = requests.post(
            url,
            auth=(USERNAME, PASSWORD),
            data=payload,
            verify=False,
            timeout=30
        )

        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text[:500])

        response.raise_for_status()

        alerts = []

        for line in response.text.splitlines():

            if not line.strip():
                continue

            try:

                record = json.loads(line)

                if "result" not in record:
                    continue

                result = record["result"]

                alerts.append({

                    "time": result.get("_time", ""),

                    "event": result.get("_raw", "Splunk Event"),

                    "ip": result.get("src_ip", "Unknown"),

                    "user": result.get("user", "Unknown"),

                    "severity": "LOW",

                    "threat": "Splunk Event",

                    "mitre": "None",

                    "status": "Detected",
 
                    "source": "Splunk"
                })

            except json.JSONDecodeError:
                continue

        print(f"✅ Splunk Alerts Retrieved: {len(alerts)}")
        print("========== SPLUNK DEBUG ==========")
        print("HTTP Status:", response.status_code)
        print("Number of alerts:", len(alerts))

        if alerts:
             print("First alert:")
             print(alerts[0])
        else:
             print("No alerts returned from Splunk")
        return alerts

    except requests.exceptions.ConnectionError:
        print("❌ Unable to connect to Splunk.")
        return []

    except requests.exceptions.Timeout:
        print("❌ Splunk request timed out.")
        return []

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return []

    except Exception as e:
        print(f"❌ Splunk Error: {e}")
        return []