# Network Firewall

**In Summary**\
These rules are written to control the traffic in between VLANs, for example traffic from VLAN 10 to internet/VLAN20 and such. 

**ALIASES:**\
InternalNetwork: 192.168.20.0/24, 192.168.10.0/24\
Network: 192.168.20.0/24, 192.168.10.0/24, 192.168.1.0/24\ 
Proxmoxs_and_PBS:  	192.168.20.2, 192.168.20.3, 192.168.20.4, 192.168.20.129\

**pfSENSE Firewall RULES:**/
*statefull rules*

**WAN:**
BLANK, NO TRAFFIC FROM OUTSIDE CAN REACH MY NETWORK

**VLAN 20:**

*Proxmox + PBS hosts ping all*
Protocol: IPv4 ICMP  
Source: Proxmoxs_and_PBS 
Destination: InternalNetwork  
Destination Port: any  

*Proxmox + PBS hosts to Active Directory*
Protocol: IPv4 TCP  
Source: Proxmoxs_and_PBS  
Destination: 192.168.10.200  
Destination Port: 636 (LDAPS)

*Proxmox + PBS hosts to Active Directory DNS*
Protocol: IPv4 TCP/UDP  
Source: Proxmoxs_and_PBS  
Destination: 192.168.10.200  
Destination Port: 53 (DNS)

*Proxmox + PBS hosts to Loki*
Protocol: IPv4 TCP  
Source: Proxmoxs_and_PBS  
Destination: 192.168.10.130  
Destination Port: 3100

*Proxmox + PBS hosts to Internet*
Protocol: IPv4 any  
Source: Proxmoxs_and_PBS  
Destination: ! Network  
Destination Port: any

**VLAN 10:**

*VLAN 10 hosts ping all*
Protocol: IPv4 ICMP
Source: VLAN10 subnets
Destination: InternalNetwork
Destination Port: any

*Active Directory DNS to ISP DNS*
Protocol: IPv4 TCP/UDP
Source: 192.168.10.200
Destination: 192.168.1.1
Destination Port: 53 (DNS)

*Monitoring VM to Node Exporter in VLAN 20*
Protocol: IPv4 TCP
Source: 192.168.10.130
Destination: Proxmoxs_and_PBS
Destination Port: 9100

*VLAN 10 hosts to Internet*
Protocol: IPv4 any
Source: VLAN10 subnets
Destination: ! Network
Destination Port: any

LAST EDIT : 7/08/2026