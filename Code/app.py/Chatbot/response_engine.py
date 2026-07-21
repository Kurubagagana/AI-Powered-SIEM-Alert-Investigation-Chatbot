def respond(alert):

    actions = []

    if alert["risk_score"] >= 80:
        actions.append("Block IP")
        actions.append("Disable User")
        actions.append("Create Ticket")
        actions.append("Notify SOC")

    elif alert["risk_score"] >= 60:
        actions.append("Notify SOC")
        actions.append("Investigate")

    else:
        actions.append("Monitor")

    return actions