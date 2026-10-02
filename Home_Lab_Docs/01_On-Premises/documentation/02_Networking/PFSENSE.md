# PfSense
   
PfSense is used as the default router by all hosts, it is a hosted internal router/firewall, its roles are:\ 
* DHCP
* Centralized VPN gateway
* Internal Router
* Network Firewall

DHCP, it is the DHCP server for the LAN, for VLAN 20, it used currently used for static mapping to the backup server (192.168.20.129), for VLAN 10, it's used for static mapping of various resources like Docker VM and Monitorging VM, and it has an address pool range from 192.168.10.240 to 192.168.10.254.\
For further information of the DHCP usage see the NETWORK DIAGRAM in the Topology Dir. 

IT acts as the VPN gateway, Tailscale is installed and enabled in PFsense, and all vpn traffic passes though PFsense, furthermore specifically to Tailscale, it acts as the Exit node and it propagates its subnets.

It acts as the internal router, being the defaul gateway of all hosts. 

The Network Firewall and aliases are defined in .../01_Security/1_Network Firewall.md in the documentation

Missing:\
redundancy




LAST EDIT : 1/10/2026