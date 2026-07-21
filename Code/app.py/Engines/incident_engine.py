def create_incidents(alerts):

    incidents = []

    grouped_alerts = {}


    # Group alerts by event
    for alert in alerts:

        event = alert.get(
            "event",
            "Unknown Event"
        )


        if event not in grouped_alerts:

            grouped_alerts[event] = []


        grouped_alerts[event].append(alert)



    incident_number = 1



    for title, alert_list in grouped_alerts.items():


        total_risk = 0


        for alert in alert_list:

            total_risk += int(
                alert.get(
                    "risk_score",
                    0
                )
            )



        risk_score = int(
            total_risk / len(alert_list)
        )



        # Severity calculation

        if risk_score >= 70:

            severity = "High"


        elif risk_score >= 40:

            severity = "Medium"


        else:

            severity = "Low"




        # Status

        if risk_score >= 40:

            status = "Investigating"

        else:

            status = "Monitoring"





        incidents.append({

            "id":
            f"INC-{incident_number:03}",


            "title":
            title,


            "severity":
            severity,


            "risk_score":
            risk_score,


            "status":
            status,


            # FIXED HERE
            "alert_count":
            len(alert_list),


            "assigned":
            "SOC Tier-1"

        })



        incident_number += 1



    return incidents