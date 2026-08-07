# Tailscale ACCESS CONTROL POLICIES: 

**In Summary**\
These rules are made to control the traffic flow between my personal devices to the internal network, to only the necessary ports and IPs, for example: SSH for Ansible, access Proxmox and pfSense GUIs and much more.


**Definitions:**\
clients = devices using Remote Access VPN\
vpngateway = Pfsense deployed on Pfsense \
Proxmoxs = IPs of Proxmox hosts (192.168.20.x[2-4])\
PFsense = IPs of PFsense interfaces (192.168.10.1;192.168.20.1;192.168.1.55)\
VLAN 10 = 192.168.10.0/24\
VLAN 20 = 192.168.20.0/24

**TAILSCALE ACCESS CONTROL POLICIES RULES:**\
*statefull rules*

*Clients to 192.168.10.3 APPLICATIONS*.\
source: clients \
dest: 192.168.10.3 \
dest ports: tcp:4533, tcp:3001, tcp:8096, tcp:8128, tcp:8920 

*CLIENTS: SSH and PING to VLAN 10*\
source: clients \
dest: VLAN10 \
dest ports: icmp:*, tcp:22 

*Clients to SSH and ping on VLAN 20*\
source: clients \
dest: VLAN20 \
dest ports: icmp:*, tcp:22 

*Clients to Proxmox GUI*\
source: clients \
dest: Proxmoxs \
dest ports: tcp:8006 

*Clients to Pfsense GUI*\
source: clients \
dest: PFsense \
dest ports: tcp:443 

*Clients to PBS*\
source: clients \
dest: 192.168.20.129 \
dest ports: tcp:8007 

*Clients to Grafana, Prometheus and Loki*\
source: clients \
dest: 192.168.10.130 \
dest ports: tcp:3000, tcp:3100, tcp:9090

LAST EDIT : 7/08/2026