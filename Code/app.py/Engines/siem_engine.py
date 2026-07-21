from indexer_api import get_latest_alerts
from splunk_api import get_splunk_alerts

def get_all_alerts():

    wazuh_alerts = get_latest_alerts()
    splunk_alerts = get_splunk_alerts()

    return {
        "wazuh": wazuh_alerts,
        "splunk": splunk_alerts
    }