import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def investigate_alert(alert):

    # Extract useful information safely
    rule = alert.get("rule", {})
    agent = alert.get("agent", {})

    description = rule.get("description", "Unknown Event")
    severity = rule.get("level", "Unknown")
    mitre = rule.get("mitre", "Not Available")
    agent_name = agent.get("name", "Unknown Host")
    ip = agent.get("ip", "Unknown IP")

    prompt = f"""
You are a Senior Security Operations Center (SOC) Analyst.

Your job is to investigate security alerts like a professional Tier-2 SOC Analyst.

Analyze the following alert.

Alert Information

Event:
{description}

Severity:
{severity}

Agent:
{agent_name}

Source IP:
{ip}

MITRE:
{mitre}

Generate a professional investigation report using the EXACT format below.

====================================================
AI SECURITY INVESTIGATION REPORT
====================================================

1. Incident Summary

Briefly explain what happened.

----------------------------------------------------

2. Risk Assessment

Include:

• Risk Score (0-100)

• Threat Level
(Critical / High / Medium / Low)

Explain why.

----------------------------------------------------

3. MITRE ATT&CK Analysis

Explain the ATT&CK technique if available.

Otherwise say:

"No MITRE ATT&CK mapping available."

----------------------------------------------------

4. Indicators of Compromise (IOCs)

List:

• Host

• IP

• Event

• Any suspicious indicators

----------------------------------------------------

5. Possible Impact

Explain what could happen if this alert represents a real attack.

----------------------------------------------------

6. Recommended Response

Provide at least 5 professional SOC response actions.

----------------------------------------------------

7. Investigation Steps

Describe how a SOC analyst should continue the investigation.

----------------------------------------------------

8. Analyst Verdict

Finish with one of these:

• Benign Event

• Suspicious Activity

• Potential Security Incident

• Confirmed Threat

Keep the report professional and concise.

Do NOT invent facts that are not present in the alert.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        return "Unable to contact the AI investigation engine."

    result = response.json()

    return result.get("response", "No response generated.")