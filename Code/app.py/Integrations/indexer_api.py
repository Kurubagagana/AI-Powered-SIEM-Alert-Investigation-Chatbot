import requests


INDEXER_URL = "https://localhost:9200"

CERT = (
    "admin.pem",
    "admin-key.pem"
)

CA_CERT = False


def get_latest_alerts():

    url = INDEXER_URL + "/wazuh-alerts-4.x-*/_search"

    query = {
        "size":10,
        "sort":[
            {
                "@timestamp":{
                    "order":"desc"
                }
            }
        ]
    }


    response = requests.get(
        url,
        json=query,
        cert=CERT,
        verify=CA_CERT
    )


    data=response.json()


    alerts=[]


    for item in data["hits"]["hits"]:
        alerts.append(
            item["_source"]
        )


    return alerts

def get_high_severity_alerts():
    ...


def get_today_alerts():
    ...


def get_alerts_by_agent(agent):
    ...


def search_alerts(keyword):
    ...

