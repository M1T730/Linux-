import requests

loki = "http://192.168.10.130:3100"
query = '{job="systemd-journal"} |~ "error"'

response = requests.get(
    f"{loki}/loki/api/v1/query_range",
    params={
        "query": query,
        "limit": 100
    }
)
data = response.json()

for result in data["data"]["result"]:
    for entry in result["values"]:
        print(entry[1])