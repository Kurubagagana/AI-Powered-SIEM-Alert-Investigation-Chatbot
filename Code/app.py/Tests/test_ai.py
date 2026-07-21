from indexer_api import get_latest_alerts
from alert_parser import parse_alert
from chatbot import investigate_alert


alerts=get_latest_alerts()


alert=parse_alert(alerts[0])


print(alert)


report=investigate_alert(alert)


print(report)