def detect_intent(question):

    question = question.lower()


    if "agent" in question:
        return "agents"


    elif "high" in question or "severity" in question:
        return "high"


    elif "mitre" in question or "attack" in question:
        return "mitre"


    elif "wazuh" in question:
        return "wazuh"


    elif "splunk" in question:
        return "splunk"


    elif "all" in question:
        return "all"


    else:
        return "chat"