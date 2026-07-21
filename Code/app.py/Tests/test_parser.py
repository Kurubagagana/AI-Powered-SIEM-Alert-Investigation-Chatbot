from indexer_api import get_latest_alerts
from alert_parser import parse_alert


alerts = get_latest_alerts()


alert = alerts[0]


parsed = parse_alert(alert)


print(parsed)