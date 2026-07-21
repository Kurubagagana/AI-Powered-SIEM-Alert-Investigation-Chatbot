from flask import Flask, render_template, request

from threat_intelligence import check_ip
from risk_engine import calculate_risk
from incident_engine import create_incidents

from indexer_api import get_latest_alerts
from splunk_api import get_splunk_alerts
from siem_engine import get_all_alerts

from alert_parser import parse_alert

from ai_investigator import investigate_alert
from chatbot import ask_llm

from intent_router import detect_intent
from response_engine import respond


import json
from collections import Counter


app = Flask(__name__)


# ======================================
# MAIN DASHBOARD
# ======================================

@app.route("/", methods=["GET","POST"])
def home():

    response = ""


    # ==========================
    # SOC CHATBOT
    # ==========================

    if request.method == "POST":

        question = request.form["question"]

        intent = detect_intent(question)


        # ==========================
        # WAZUH AGENTS
        # ==========================

        if intent == "agents":

            alerts = get_latest_alerts()

            agents = set()

            for alert in alerts:

                if "agent" in alert:
                    agents.add(alert["agent"]["name"])


            response = "Available Wazuh Agents\n\n"

            for agent in sorted(agents):

                response += f"- {agent}\n"



        # ==========================
        # HIGH ALERTS
        # ==========================

        elif intent == "high":

            alerts = get_latest_alerts()

            high = []

            for alert in alerts:

                if alert["rule"]["level"] >= 5:

                    high.append(alert)


            response = f"High Severity Alerts : {len(high)}"



        # ==========================
        # MITRE
        # ==========================

        elif intent == "mitre":

            alerts = get_latest_alerts()

            response = "MITRE Alerts\n\n"

            found = False


            for alert in alerts:

                if "mitre" in alert.get("rule", {}):

                    found = True

                    response += (
                        alert["rule"]["description"]
                        + "\n"
                    )


            if not found:

                response += "No MITRE alerts found"



        # ==========================
        # WAZUH COUNT
        # ==========================

        elif intent == "wazuh":

            alerts = get_latest_alerts()

            response = f"Wazuh Alerts : {len(alerts)}"



        # ==========================
        # SPLUNK COUNT
        # ==========================

        elif intent == "splunk":

            splunk = get_splunk_alerts()

            response = f"Splunk Alerts : {len(splunk)}"



        # ==========================
        # ALL SIEM
        # ==========================

        elif intent == "all":

            alerts = get_all_alerts()

            response = (

                f"Wazuh Alerts : {len(alerts['wazuh'])}\n"
                f"Splunk Alerts : {len(alerts['splunk'])}"

            )



        # ==========================
        # AI SOC ASSISTANT
        # ==========================

        else:

            prompt = f"""

You are a Senior SOC Analyst.

User Question:

{question}


Provide:

1. Incident Summary

2. Risk Level

3. Investigation Steps

4. Recommended Actions

"""


            print("===== PROMPT =====")

            print(prompt)


            response = ask_llm(prompt)


            print("===== RESPONSE =====")

            print(response)



    # ==============================
    # LOAD ALERTS
    # ==============================


    alerts=get_latest_alerts()


    parsed_alerts=[]


    for alert in alerts:


        parsed=parse_alert(alert)



        # Risk Engine

        risk=calculate_risk(parsed)


        parsed["risk_score"]=risk["score"]

        parsed["risk_level"]=risk["level"]



        # Threat Intelligence


        try:

            intel=check_ip(parsed["ip"])

            parsed["country"]=intel["country"]

            parsed["abuse_score"]=intel["score"]

            parsed["reputation"]=intel["reputation"]


        except Exception as e:
            print(e)

            parsed["country"]="Unknown"

            parsed["abuse_score"]=0

            parsed["reputation"]="Unknown"



        # Automated Response


        parsed["response"]=respond(parsed)



        parsed_alerts.append(parsed)



    # Incident creation

    incidents=create_incidents(parsed_alerts)



    # Counts

    wazuh_count=len(parsed_alerts)


    splunk_alerts=get_splunk_alerts()

    splunk_count=len(splunk_alerts)


    total_alerts=wazuh_count+splunk_count



    high_alerts=0


    for alert in parsed_alerts:

        if int(alert["severity"]) >=5:

            high_alerts+=1



    # ==============================
    # CHART DATA
    # ==============================


    severity_count=Counter()



    for alert in parsed_alerts:


        severity=int(alert["severity"])


        if severity>=5:

            severity_count["HIGH"]+=1


        elif severity>=3:

            severity_count["MEDIUM"]+=1


        else:

            severity_count["LOW"]+=1




    source_count={

        "Wazuh":wazuh_count,

        "Splunk":splunk_count

    }



    mitre_count=Counter()



    for alert in parsed_alerts:


        mitre=alert["mitre"]


        if isinstance(mitre,dict):


            ids=mitre.get("id",[])


            for item in ids:

                mitre_count[item]+=1


        elif mitre!="None":

            mitre_count[str(mitre)]+=1





    return render_template(

        "index.html",

        alerts=parsed_alerts,

        incidents=incidents,

        response=response,


        total_alerts=total_alerts,

        wazuh_count=wazuh_count,

        splunk_count=splunk_count,

        high_alerts=high_alerts,


        severity_labels=json.dumps(list(severity_count.keys())),

        severity_values=json.dumps(list(severity_count.values())),


        source_labels=json.dumps(list(source_count.keys())),

        source_values=json.dumps(list(source_count.values())),


        mitre_labels=json.dumps(list(mitre_count.keys())[:5]),

        mitre_values=json.dumps(list(mitre_count.values())[:5])

    )




# ======================================
# AI INVESTIGATION PAGE
# ======================================


@app.route("/investigate/<int:id>")
def investigate(id):


    alerts=get_latest_alerts()


    alert=parse_alert(alerts[id])


    risk=calculate_risk(alert)


    alert["risk_score"]=risk["score"]

    alert["risk_level"]=risk["level"]



    try:

        intel=check_ip(alert["ip"])

        alert["country"]=intel["country"]

        alert["abuse_score"]=intel["score"]

        alert["reputation"]=intel["reputation"]


    except Exception:

        alert["country"]="Unknown"

        alert["abuse_score"]=0

        alert["reputation"]="Unknown"



    report=investigate_alert(alert)
 



    return render_template(

        "investigation.html",

        alert=alert,

        report=report

    )





if __name__=="__main__":


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )