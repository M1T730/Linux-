# Monitoring and Logging with Prometheus, Loki and Grafana

**Prereq:**
create a vm/lxc
install docker

**step 1:**
create the docker compose file + promethous and loki config file:

docker-compose.yml
```yaml
version: "3.8"

services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    ports:
      - "9090:9090"
    restart: unless-stopped

  loki:
    image: grafana/loki:latest
    command: -config.file=/etc/loki/local-config.yaml
    volumes:
      - ./loki-config.yaml:/etc/loki/local-config.yaml
      - loki_data:/loki
    ports:
      - "3100:3100"
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    restart: unless-stopped

volumes:
  prometheus_data:
  loki_data:
  grafana_data: 
```
loki-config.yml:

```yaml
auth_enabled: false

server:
  http_listen_port: 3100

common:
  path_prefix: /loki
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

storage_config:
  filesystem:
    directory: /loki/chunks

schema_config:
  configs:
    - from: 2024-01-01
      store: tsdb
      object_store: filesystem
      schema: v13
      index:
        prefix: index_
        period: 24h

limits_config:
  allow_structured_metadata: true
```
prometheus.yml:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "nodes"
    static_configs:
      - targets:
         - 192.168.10.1:9100
         - 192.168.20.1:9100
         - 192.168.20.2:9100
         - 192.168.10.2:9100
         - 192.168.10.3:9100
         - 192.168.10.129:9100
         - 192.168.10.130:9100
```

**step 2:**
install node explorer on everynode and vm (explained in stage 3 1_Ansible) for prometheus
**step 3:**
install promtrail on everynode and vm (explained in stage 3 1_Ansible)

**step 4:**
setup grafana with loki and prometheus as source data and import dashboards from internet