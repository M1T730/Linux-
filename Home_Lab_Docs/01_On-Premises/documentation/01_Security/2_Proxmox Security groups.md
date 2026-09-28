# Proxmox Security groups, hypervisor level firewall

**In Summary**\
These rules dictate all the traffic that is permitted IN and OUT of each VM/LXC and proxmox host.\
(I will not explain every SG, it would take too long)

**ALIASES:**\
AD: 192.168.10.200 | Active Directory Domain Controller\
ML: 192.168.10.130 | Monitoring VM\
PBS: 192.168.20.129 | Proxmox Backup Server\
PDM: 192.168.20.254 | Proxmox Datacenter Manager\
VLAN10: 192.168.10.0/24 | VLAN 10\
VLAN20: 192.168.20.0/24 | VLAN 20\
docker 192.168.10.3 | Docker VM\
node1: 192.168.20.2\
node2: 192.168.20.3\
node3: 192.168.20.4\
OfflineME 192.168.20.100 | Me when I connect myself to the switch with the cable (NO VPN)

**SECURITY GROUPS:**\
(divided by scope):\
(for some the sources or destination will be aggregated)

**Internet:**\
rule 0-1:\
Type: out\
Action: DROP\
Macro:\
Protocol:\
Source: vlan10 and vlan20\
Source Port:\
Destination:\
Destination Port:

rule 2:\
Type: out\
Action: ACCEPT\
Macro:\
Protocol:\
Source: \
Source Port:\
Destination:\
Destination Port:

**AD auth:**\
rule 0-3:\
Type: in\
Action: ACCEPT\
Macro: LDAPS\
Protocol:\
Source: node1, node 2, node 3 and PBS\
Source Port:\
Destination:\
Destination Port:

rule 4-7:\
Type: out\
Action: ACCEPT\
Macro: LDAPS\
Protocol:\
Source: node1, node 2, node 3 and PBS\
Source Port:\
Destination:\
Destination Port:

**Prometheus scraping from node_exporter:**\
rule 0:\
Type: out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: ML\
Source Port:\
Destination:\
Destination Port: 9100

rule 1:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: ML\
Source Port:\
Destination:\
Destination Port: 9100

**Proxmoxs to PBS:**\
rule 0-2:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: node1, node2 and node3\
Source Port:\
Destination:\
Destination Port: 8007

rule 3-5:\
Type: out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: node1, node2 and node3\
Source Port:\
Destination:\
Destination Port: 8007

**SAMBA:**\
rule 0:\
Type: in\
Action: ACCEPT\
Macro: tcp\
Protocol:\
Source: vlan10\
Source Port: \
Destination:vlan10\
Destination Port: 445

rule 1:\
Type: in\
Action: ACCEPT\
Macro: tcp\
Protocol:\
Source: ad\
Source Port: \
Destination:vlan10\
Destination Port: 445

**VPN CLIENTS SSH into hosts:**\
rule 0-1:\
Type: out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: node2\
Source Port:\
Destination: node1 and node3\
Destination Port: 22

rule 2:\
Type: in\
Action: ACCEPT\
Macro: SSH\
Protocol:\
Source: OfflineME\
Source Port:\
Destination:\
Destination Port:

rule 3-4:\
Type: in\
Action: ACCEPT\
Macro: SSH\
Protocol:\
Source: 192.168.10.1 and 192.168.20.1\
Source Port:\
Destination:\
Destination Port:

**access Proxmox GUI,  PBS GUI and PDM:**\
rule 0-1:\
Type: out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: node2\
Source Port:\
Destination: node1 and node3\
Destination Port: 8006

rule 2-3:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: OfflineME and 192.168.20.1\
Source Port:\
Destination: PBS\
Destination Port: 8007

rule 4:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: OfflineME\
Source Port:\
Destination: PBS\
Destination Port: 8006

rule 5-7:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: 192.168.20.1\
Source Port:\
Destination: node1, node2 and node3\
Destination Port: 8006

rule 8-9:\
Type: in/out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: PDM\
Source Port:\
Destination: 192.168.20.0/29\
Destination Port: 8006

rule 10-11:\
Type: in/out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: PDM\
Source Port:\
Destination: PBS\
Destination Port: 8007

**access to applications like navidrome ecc..:**\
rule 0-4:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: 192.168.10.1\
Source Port:\
Destination: docker\
Destination Port: 80

**getDNS:**
rule 0-1:\
Type: in\
Action: ACCEPT\
Macro: DNS\
Protocol:\
Source: VLAN10 and VLAN20\
Source Port:\
Destination: AD\
Destination Port:

rule 2-3:\
Type: out\
Action: ACCEPT\
Macro: DNS\
Protocol:\
Source: VLAN10 and VLAN20\
Source Port:\
Destination: AD\
Destination Port:

rule 4:\
Type: in and out\
Action: ACCEPT\
Macro: DNS\
Protocol:\
Source: AD\
Source Port:\
Destination: 192.168.1.1\
Destination Port:

**ping all hosts:**\
rule 0-1:\
Type: in\
Action: ACCEPT\
Macro: PING\
Protocol:\
Source: \
Source Port:\
Destination: VLAN10 and VLAN20\
Destination Port:

rule 2-3:\
Type: out\
Action: ACCEPT\
Macro: PING\
Protocol:\
Source: VLAN 10 and VLAN20\
Source Port:\
Destination: \
Destination Port:

rule 4-5:\
Type: in and out\
Action: ACCEPT\
Macro: Trcrt\
Protocol:\
Source: \
Source Port:\
Destination: \
Destination Port:

**send logs to Loki Though Promtrail:**\
rule 0-1:\
Type: in and out\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: \
Source Port:\
Destination: ML\
Destination Port:3100

**vpn clients to ML API points:**\
rule 0-2:\
Type: in\
Action: ACCEPT\
Macro:\
Protocol: tcp\
Source: 192.168.10.1\
Source Port:\
Destination: ML\
Destination Port: 3100, 3000, 9090

**Quorum between Proxmox hosts:**\
rule 0-1:\
Type: in and out\
Action: ACCEPT\
Macro:\
Protocol: udp\
Source: vlan20\
Source Port: \
Destination: vlan20\
Destination Port: 5405:5412

**rdp to ad**\
rule 0-1:\
Type: in and out\
Action: ACCEPT\
Macro: RDP\
Protocol:\
Source: 192.168.10.1\
Source Port: \
Destination: AD\
Destination Port: 

**clients to pdm**\
rule 0-1:\
Type: in and out\
Action: ACCEPT\
Macro: tcp\
Protocol:\
Source: 192.168.20.1\
Source Port: \
Destination:pdm\
Destination Port: 8443


LAST EDIT : 11/09/2026