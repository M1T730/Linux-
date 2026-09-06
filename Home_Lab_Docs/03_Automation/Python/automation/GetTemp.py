import requests 

prometheus = "http://192.168.10.130:9090/" 
query = 'node_hwmon_temp_celsius'

response = requests.get(
    f'{prometheus}api/v1/query',
    params={'query':query}
)

data = response.json()

for result in data['data']['result']:
    node = result['metric']['instance']
    temperature = result['value'][1]
    chip = result['metric']['chip']
    if temperature is not None and float(temperature) > 80:
        print(f"Warning: {node} {chip} temperature is {temperature}°C")
    elif temperature is not None and float(temperature) > 70:
        print(f"Notice: {node} {chip} temperature is {temperature}°C")
    elif temperature is not None and float(temperature) > 60:
        print(f"Info: {node} {chip} temperature is {temperature}°C")
    elif temperature is not None and float(temperature) > 50:
        print(f"Debug: {node} temperature is {temperature}°C")
