def detect_intent(question):

    question = question.lower()

    if "splunk" in question:
        return "splunk"

    elif "wazuh" in question:
        return "wazuh"

    elif "all alerts" in question:
        return "all"

    elif "investigate" in question:
        return "investigate"

    else:
        return "chat"